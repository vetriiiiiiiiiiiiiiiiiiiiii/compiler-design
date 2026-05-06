import ply.lex as lex

# List of token names
tokens = (
    'LET', 'MOVE', 'FORWARD', 'BACKWARD', 'TURN', 'LEFT', 'RIGHT', 'PRINT', 'IF', 'WHILE', 'END',
    'ID', 'NUMBER',
    'EQ', 'GT', 'LT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'COMMENT'
)

# Reserved words
reserved = {
    'LET': 'LET',
    'MOVE': 'MOVE',
    'FORWARD': 'FORWARD',
    'BACKWARD': 'BACKWARD',
    'TURN': 'TURN',
    'LEFT': 'LEFT',
    'RIGHT': 'RIGHT',
    'PRINT': 'PRINT',
    'IF': 'IF',
    'WHILE': 'WHILE',
    'END': 'END'
}

# Regular expression rules for simple tokens
t_EQ = r'='
t_GT = r'>'
t_LT = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# A regular expression rule for identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# A regular expression rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Comments (ignore)
def t_COMMENT(t):
    r'\#.*'
    pass  # No return value. Token discarded

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()