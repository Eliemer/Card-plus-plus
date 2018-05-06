import ply.lex as lex
import ply.yacc as yacc

# All lex rules

# List of tokens
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'TRUE',
    'FALSE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LTHAN',
    'GTHAN',
    'LTHANOREQUALS',
    'GTHANOREQUALS',
    'ISEQUALS',
    'EQUALS',
    'COMA',
    'COLON',
    'SEMICOLON',
    'IDENTIFIER'
]

reserved = {
    'Deck' : 'DECK',
    'Field' : 'FIELD',
    'Player' : 'PLAYER',
    'Card' : 'CARD',
    'Action' : 'ACTION',
    'Actions' : 'ACTIONS',
    'Rule' : 'RULE',
    'Rules' : 'RULES'
}

operators = {
    'For' : 'FOR',
    'In' : 'IN',
    'To' : 'TO',
    'Of' : 'OF',
    'From' : 'FROM',
    'While' : 'WHILE',
    'Conditioned' : 'CONDITIONED'
}

tokens += reserved.values()
tokens += operators.values()

# Regular Expressions for tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_TRUE = 'True'
t_FALSE = 'False'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LTHAN = r'<'
t_GTHAN = r'>'
t_LTHANOREQUALS = r'\<\='
t_GTHANOREQUALS = r'\>\='
t_ISEQUALS = r'\=\='
t_EQUALS = r'\='
t_COMA = r','
t_COLON = r'\:'
t_SEMICOLON = r';'

def t_NUMBER(t):
    r'\d+'
    try :
        t.value = int(t.value)
    except ValueError:
        print("Line %d: Number %s is too large" % (t.lineno, t.value))
        t.value = 0
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z0-9]+'
    if t.value in operators:
        t.type = operators[ t.value ]
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# TEST DATA
data = '''
Deck { a, b, c, d, e}

this == 3
that >= 2
'''

# lex.input(data)

# while 1:
#     tok = lex.token()
#     if not tok: break
#     print(tok)

# All parse rules

# -----------------------------------------------------------------------------
#
#
#
# -----------------------------------------------------------------------------

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS')
)

identifiers = {}

def p_statement_assign(t):
    'statement : IDENTIFIER EQUALS expression'
    identifiers[t[1]] = t[3]


def p_statement_expr(t):
    '''statement : expression
                 | boolean_statement'''
    print(t[1])

def p_boolean_statement(t):
    '''boolean_statement : TRUE
                         | FALSE
                         | expression ISEQUALS expression
                         | expression GTHAN expression
                         | expression LTHAN expression
                         | expression GTHANOREQUALS expression
                         | expression LTHANOREQUALS expression'''
    if t[1] == 'True':
        t[0] = True
    elif t[1] == 'False':
        t[0] = False
    elif t[2] == '==':
        t[0] = t[1] == t[3]
    elif t[2] == '>':
        t[0] = t[1] > t[3]
    elif t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '>=':
        t[0] = t[1] >= t[3]
    elif t[2] == '<=':
        t[0] = t[1] <= t[3]


def p_expression_binary_operations(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_uplus(t):
    'expression : PLUS expression %prec UPLUS'
    t[0] = t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_identifier(t):
    'expression : IDENTIFIER'
    try:
        t[0] = identifiers[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

# def p_list(t):
#     '''list : expression'''
#
# def p_parenthesis_expression(t):
#     'expression : LPAREN expression RPAREN'
#     t[0] = t[2]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('card >')
    except EOFError:
        break
    parser.parse(s)