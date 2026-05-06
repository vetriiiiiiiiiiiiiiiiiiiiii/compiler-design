class ASTNode:
    pass

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class LetNode(ASTNode):
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class MoveNode(ASTNode):
    def __init__(self, direction, expr):
        self.direction = direction  # 'FORWARD' or 'BACKWARD'
        self.expr = expr

class TurnNode(ASTNode):
    def __init__(self, direction, expr):
        self.direction = direction  # 'LEFT' or 'RIGHT'
        self.expr = expr

class IfNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

class VariableNode(ASTNode):
    def __init__(self, name):
        self.name = name