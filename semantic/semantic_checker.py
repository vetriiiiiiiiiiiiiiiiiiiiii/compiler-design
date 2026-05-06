from ast_nodes.nodes import *

class SemanticChecker:
    def __init__(self):
        self.symbol_table = {}
        self.errors = []

    def check(self, ast):
        self.visit(ast)
        return self.errors

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in self.get_children(node):
            self.visit(child)

    def get_children(self, node):
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
        elif isinstance(node, (NumberNode, VariableNode)):
            return []
        return []

    def visit_LetNode(self, node):
        self.visit(node.expr)
        if node.var_name in self.symbol_table:
            self.errors.append(f"Variable '{node.var_name}' already declared")
        else:
            self.symbol_table[node.var_name] = 'int'  # Assume int type

    def visit_VariableNode(self, node):
        if node.name not in self.symbol_table:
            self.errors.append(f"Undefined variable '{node.name}'")

    def visit_BinaryOpNode(self, node):
        self.visit(node.left)
        self.visit(node.right)
        # Assume all operations are on ints