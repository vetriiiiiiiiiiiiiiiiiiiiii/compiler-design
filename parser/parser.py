import ply.yacc as yacc
from lexer.lexer import tokens
from ast_nodes.nodes import *

# Grammar rules

def p_program(p):
    'program : statements'
    p[0] = ProgramNode(p[1])

def p_statements(p):
    '''statements : statement statements
                  | statement'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : let_stmt
                 | print_stmt
                 | move_stmt
                 | turn_stmt
                 | if_stmt
                 | while_stmt'''
    p[0] = p[1]

def p_let_stmt(p):
    'let_stmt : LET ID EQ expr'
    p[0] = LetNode(p[2], p[4])

def p_print_stmt(p):
    'print_stmt : PRINT expr'
    p[0] = PrintNode(p[2])

def p_move_stmt(p):
    'move_stmt : MOVE direction expr'
    p[0] = MoveNode(p[2], p[3])

def p_turn_stmt(p):
    'turn_stmt : TURN direction expr'
    p[0] = TurnNode(p[2], p[3])

def p_direction_move(p):
    '''direction : FORWARD
                 | BACKWARD'''
    p[0] = p[1]

def p_direction_turn(p):
    '''direction : LEFT
                 | RIGHT'''
    p[0] = p[1]

def p_if_stmt(p):
    'if_stmt : IF condition statements END'
    p[0] = IfNode(p[2], p[3])

def p_while_stmt(p):
    'while_stmt : WHILE condition statements END'
    p[0] = WhileNode(p[2], p[3])

def p_condition(p):
    '''condition : expr GT expr
                 | expr LT expr'''
    p[0] = BinaryOpNode(p[1], p[2], p[3])

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''
    if len(p) == 4:
        p[0] = BinaryOpNode(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 4:
        p[0] = BinaryOpNode(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | ID
              | LPAREN expr RPAREN'''
    if p[1] == '(':
        p[0] = p[2]
    else:
        if isinstance(p[1], int):
            p[0] = NumberNode(p[1])
        else:
            p[0] = VariableNode(p[1])

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()