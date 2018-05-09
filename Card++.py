import ply.lex as lex
import ply.yacc as yacc

# All lex rules

# List of tokens
tokens = [
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LSBRACKET',
    'RSBRACKET',
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
    'Rules' : 'RULES',
    'True' : 'TRUE',
    'False' : 'FALSE'
}

operators = {
    'And' : 'AND',
    'Or' : 'OR',
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
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LSBRACKET = r'\['
t_RSBRACKET = r'\]'
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

def t_STRING(t):
    '\"([^"])*\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print("Line %d: String %s is poorly formatted" % (t.lineno, t.value))
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
"This is a string"
'''

# lex.input(data)
#
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
    ('left', 'OR', 'AND'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS')
)

identifiers = {}

def p_statement_assign(t):
    '''statement : IDENTIFIER EQUALS expression
                 | IDENTIFIER EQUALS boolean_and_or
                 | IDENTIFIER EQUALS string'''
    identifiers[t[1]] = t[3]
    print(t[3])

def p_statemtent_return_index(t):
    '''statement : IDENTIFIER LSBRACKET NUMBER RSBRACKET'''
    t[0] = identifiers[t[1]][t[3]]
    print(t[0])

# def p_code_block_assign(t):
#     'block : IDENTIFIER LBRACKET expression RBRACKET'
#     identifiers[t[1]] = t[3]


def p_statement_expr(t):
    '''statement : expression
                 | boolean_and_or
                 | string'''
    print(t[1])

def p_boolean_and_or_operations(t):
    '''boolean_and_or : boolean_statement
                      | boolean_statement AND boolean_statement
                      | boolean_statement OR boolean_statement'''
    if len(t) == 2:
        t[0] = t[1]
    elif t[2] == 'And':
        t[0] = t[1] and t[3]
    elif t[2] == 'Or':
        t[0] = t[1] or t[3]

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

def p_string_statement(t):
    '''string : STRING'''
    t[0] = t[1]

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

def p_expression_tuple(t):
    'expression : tuple_expression'
    t[0] = t[1]

def p_tuple_expression(t):
    '''tuple_expression : LPAREN tuple_content RPAREN
                        | LPAREN tuple_expression RPAREN COMA tuple_expression'''
    t[0] = t[2]

def p_tuple_content(t):
    '''tuple_content :
                     | tuple_content COMA tuple_item
                     | tuple_item'''
    if len(t) == 1:
        t[0] = ()
    elif len(t) == 2:
        t[0] = (t[1],)
    else:
        t[0] = t[1] + (t[3],)

def p_tuple_item(t):
    '''tuple_item : expression
                  | boolean_and_or
                  | string'''
    t[0] = t[1]

def p_expression_list(t):
    '''expression : list_expression'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = [t[1], t[3]]

def p_list_expression(t):
    '''list_expression : LBRACKET list_content RBRACKET
                       | LBRACKET list_expression RBRACKET COMA list_expression'''
    t[0] = t[2]

def p_list_content(t):
    '''list_content :
                    | list_content COMA list_item
                    | list_item '''
    if len(t) == 1:
        t[0] = []
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]

def p_list_item(t):
    '''list_item : expression
                 | boolean_and_or
                 | string'''
    t[0] = t[1]

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