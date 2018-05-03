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
    'LPAREN',
    'RPAREN',
    'LTHAN',
    'GTHAN',
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
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LTHAN = r'<'
t_GTHAN = r'>'
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
3 + 4 * 80
iden + 7 - ident

Actions:
    Action Draw(t):
        at the start of turn, add card to Player hand;
    for() FOR
    while Action Actions
    P1 Rule Rules
    1 + 8 = 9 while 7 > 97
'''

lex.input(data)

while 1:
    tok = lex.token()
    if not tok: break
    print(tok)

# All parse rules


# Build the parser
#parser = yacc.yacc()
