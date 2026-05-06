from llvmlite import ir
from ast_nodes.nodes import *

class LLVMIRGenerator:
    def __init__(self):
        self.module = ir.Module(name="roboscript")
        self.builder = None
        self.func = None
        self.symbol_table = {}
        self.printf_func = None

    def generate(self, ast):
        # Declare printf
        printf_type = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
        self.printf_func = ir.Function(self.module, printf_type, name="printf")

        # Create main function
        main_type = ir.FunctionType(ir.IntType(32), [])
        self.func = ir.Function(self.module, main_type, name="main")
        block = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        self.visit(ast)

        # Return 0
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

        return str(self.module)

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in self.get_children(node):
            self.visit(child)

    def get_children(self, node):
        # Similar to semantic checker
        if isinstance(node, ProgramNode):
            return node.statements
        elif isinstance(node, LetNode):
            return [node.expr]
        elif isinstance(node, PrintNode):
            return [node.expr]
        elif isinstance(node, MoveNode):
            return [node.expr]
        elif isinstance(node, TurnNode):
            return [node.expr]
        elif isinstance(node, IfNode):
            return [node.condition] + node.body
        elif isinstance(node, WhileNode):
            return [node.condition] + node.body
        elif isinstance(node, BinaryOpNode):
            return [node.left, node.right]
        return []

    def visit_LetNode(self, node):
        value = self.visit(node.expr)
        ptr = self.builder.alloca(ir.IntType(32), name=node.var_name)
        self.builder.store(value, ptr)
        self.symbol_table[node.var_name] = ptr

    def visit_PrintNode(self, node):
        value = self.visit(node.expr)
        # Print as %d\n
        fmt = self.builder.global_string_constant("%d\n", name="fmt")
        self.builder.call(self.printf_func, [fmt, value])

    def visit_MoveNode(self, node):
        value = self.visit(node.expr)
        dir_str = "Moving " + node.direction.lower()
        fmt = self.builder.global_string_constant(dir_str + " %d\n", name="move_fmt")
        self.builder.call(self.printf_func, [fmt, value])

    def visit_TurnNode(self, node):
        value = self.visit(node.expr)
        dir_str = "Turning " + node.direction.lower()
        fmt = self.builder.global_string_constant(dir_str + " %d\n", name="turn_fmt")
        self.builder.call(self.printf_func, [fmt, value])

    def visit_IfNode(self, node):
        cond = self.visit(node.condition)
        then_block = self.func.append_basic_block("then")
        else_block = self.func.append_basic_block("else")
        merge_block = self.func.append_basic_block("merge")

        self.builder.cbranch(cond, then_block, else_block)

        self.builder.position_at_end(then_block)
        for stmt in node.body:
            self.visit(stmt)
        self.builder.branch(merge_block)

        self.builder.position_at_end(else_block)
        self.builder.branch(merge_block)

        self.builder.position_at_end(merge_block)

    def visit_WhileNode(self, node):
        loop_cond_block = self.func.append_basic_block("loop_cond")
        loop_body_block = self.func.append_basic_block("loop_body")
        after_loop_block = self.func.append_basic_block("after_loop")

        self.builder.branch(loop_cond_block)

        self.builder.position_at_end(loop_cond_block)
        cond = self.visit(node.condition)
        self.builder.cbranch(cond, loop_body_block, after_loop_block)

        self.builder.position_at_end(loop_body_block)
        for stmt in node.body:
            self.visit(stmt)
        self.builder.branch(loop_cond_block)

        self.builder.position_at_end(after_loop_block)

    def visit_BinaryOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        # Constant folding
        if isinstance(left, ir.Constant) and isinstance(right, ir.Constant):
            if node.op == '+':
                return ir.Constant(ir.IntType(32), left.constant + right.constant)
            elif node.op == '-':
                return ir.Constant(ir.IntType(32), left.constant - right.constant)
            elif node.op == '*':
                return ir.Constant(ir.IntType(32), left.constant * right.constant)
            elif node.op == '/':
                return ir.Constant(ir.IntType(32), left.constant // right.constant)  # integer div
            elif node.op == '>':
                return ir.Constant(ir.IntType(1), left.constant > right.constant)
            elif node.op == '<':
                return ir.Constant(ir.IntType(1), left.constant < right.constant)
        # Else generate IR
        if node.op == '+':
            return self.builder.add(left, right)
        elif node.op == '-':
            return self.builder.sub(left, right)
        elif node.op == '*':
            return self.builder.mul(left, right)
        elif node.op == '/':
            return self.builder.sdiv(left, right)
        elif node.op == '>':
            return self.builder.icmp_signed('>', left, right)
        elif node.op == '<':
            return self.builder.icmp_signed('<', left, right)

    def visit_NumberNode(self, node):
        return ir.Constant(ir.IntType(32), node.value)

    def visit_VariableNode(self, node):
        ptr = self.symbol_table[node.name]
        return self.builder.load(ptr)