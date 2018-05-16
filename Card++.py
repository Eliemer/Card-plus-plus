import ply.lex as lex
import ply.yacc as yacc
import GameElements.Card as card
import GameElements.Field as field
import GameElements.Player as player

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
    'IDENTIFIER',
    'NEWLINE'
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
# t_NEWLINE = r'[^\r\n]'

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

def t_NEWLINE(t):
    r'\n+'
    t.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# TEST DATA
data = '''"This is a string"


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
    ('right', 'UPLUS'),
)

identifiers = {}
rules = {}
actions = {}
cards = {}

def p_program(t):
    '''program : statements'''

def p_statements(t):
    '''statements : statement SEMICOLON
                  | statements statement SEMICOLON'''


def p_statement_assign(t):
    '''statement_assign : IDENTIFIER EQUALS expression
                        | IDENTIFIER EQUALS boolean_and_or
                        | IDENTIFIER EQUALS string'''
    identifiers[t[1]] = t[3]
    print(t[3])

def p_action_statement_assign(t):
    '''action_statement : ACTION IDENTIFIER LPAREN action_parameters RPAREN LBRACKET action_content SEMICOLON RBRACKET'''
    actions[t[2]] = t[4]
    identifiers[t[2]] = t[4]
    t[0] = t[4]

def p_action_content(t):
    '''action_content : function
                      | action_content SEMICOLON function'''
    if len(t) == 2:
        t[0] = t[1]

def p_card_type_declaration(t):
    '''card_declaration : CARD IDENTIFIER EQUALS tuple_expression'''
    if len(t[4]) == 2:
        t[0] = card.Card(t[4][0], t[4][1])
        identifiers[t[2]] = t[0]
        cards[t[2]] = t[0]

def p_function(t):
    '''function : IDENTIFIER LPAREN action_parameters RPAREN'''
    if t[1] == "Flip" or t[1] == "flip":
        if isinstance(t[3][0], tuple):
            # t[0] = flip(t[3][0])
            try:
                c = card.Card(t[3][0][0], t[3][0][1])
                print("Flipping")
                c.flip()
                print(c.getValue() + " of " + c.getSuit())
                t[0] = ""
            except IndexError:
                print("bad")
        else:
            print("Can only flip card tuples")
    elif t[1] == "Move" or t[1] == "move":
        if isinstance(t[3], list):
            if isinstance(t[3][0], list) and isinstance(t[3][1], list):
                try:
                    if isinstance(t[3][2], tuple):
                        t[0] = move([t[3][0], t[3][1], t[3][2]])

                except IndexError:
                    t[0] = move([t[3][0], t[3][1]])

            else:
                print("Origin or destination is not defined as a field")
        else:
            print("move() undefined for such parameter")
    elif t[1] == "Compare" or t[1] == "compare":
        if len(t[3]) == 2:
            if isinstance(t[3][0], tuple) and isinstance(t[3][1], tuple):
                compare(t[3][0], t[3][1])
            else:
                print("Parameters must be tuples")
        else:
            print("Incorrect number of parameters for Compare()")




def p_action_parameters(t):
    '''action_parameters : action_parameter
                         | action_parameters COMA action_parameter'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]


def p_action_parameter(t):
    '''action_parameter : expression'''
    t[0] = t[1]

def p_statement_verify(t):
    '''statement : verify'''
    print(t[1])

def p_verify_statement(t):
    '''verify : IDENTIFIER IDENTIFIER'''
    if len(t) == 3:
        if t[1] == "verify" or t[1] == "Verify":
            try:
                t[0] = eval(eval(rules[t[2]]))
            except KeyError:
                try:
                    print("Rule $s does not exist" % t[2])
                except TypeError:
                    print("Undefined parameters used")
            except NameError:
                print("Malformed rule expression")


def p_rule_statement_assign(t):
    '''rule_statement : RULE IDENTIFIER string
                      | RULE IDENTIFIER
                      | RULE'''
    if len(t) == 2:
        print("Empty Rule Declaration")
    elif len(t) == 3:
        try:
            t[0] = rules[t[2]]
        except KeyError:
            print("Rule %s does not exist" % t[2])
    elif len(t) == 4:
        try:
            rules[t[2]] = t[3]
            identifiers[t[2]] = rules[t[2]]
            t[0] = rules[t[2]]
        except AttributeError:
            print("Empty Rule Declaration")

def p_rules_statement_block(t):
    '''rules_block : RULES LBRACKET rule_statements RBRACKET
                   | RULES'''
    if len(t) == 2:
        t[0] = rules
    else:
        t[0] = t[3]

def p_rules_statements(t):
    '''rule_statements : rule_statement
                       | rule_statements COMA rule_statement'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]

def p_statemtent_return_index(t):
    '''statement : IDENTIFIER LSBRACKET NUMBER RSBRACKET'''
    t[0] = identifiers[t[1]][t[3]]
    print(t[0])

# def p_code_block_assign(t):
#     'block : IDENTIFIER LBRACKET expression RBRACKET'
#     identifiers[t[1]] = t[3]


def p_statement_expr(t):
    '''statement :
                 | statement_assign
                 | card_declaration
                 | action_statement
                 | function
                 | rules_block
                 | rule_statement
                 | expression
                 | boolean_and_or
                 | string'''
    if len(t) == 2:
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
    if len(t) == 1:
        t[0] = None
    else:
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
        try:
            t[0] = t[1] / t[3]
        except ZeroDivisionError:
            print("Cannot divide by zero")

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
    '''tuple_content : tuple_content COMA tuple_item
                     | tuple_item'''
    if len(t) == 2:
        t[0] = (t[1],)
    else:
        t[0] = t[1] + (t[3],)

def p_tuple_item(t):
    '''tuple_item :
                  | expression
                  | boolean_and_or
                  | string'''
    if len(t) == 1:
        t[0] = ()
    elif len(t) == 2:
        t[0] = t[1]

def p_expression_list(t):
    '''expression : list_expression'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = [t[1], t[3]]

def p_list_expression(t):
    '''list_expression : LSBRACKET list_content RSBRACKET
                       | LSBRACKET list_expression RSBRACKET COMA list_expression'''
    t[0] = t[2]

def p_list_content(t):
    '''list_content : list_content COMA list_item
                    | list_item '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]

def p_list_item(t):
    '''list_item :
                 | expression
                 | boolean_and_or
                 | string'''
    if len(t) == 1:
        t[0] = []
    elif len(t) == 2:
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

def parsing(file):
    def get_token():
        '''a tokenizer that automatically feeds the lexer with the next line'''
        while True:
            tok = lex.token()
            if tok is not None: return tok
            try:
                line = next(file)
                lex.input(line)
            except StopIteration:
                return None
    parser.parse("", lexer=lex, tokenfunc=get_token)

def move(a):
    if len(a) == 2:
        print("random moving")
        return True
    elif len(a) == 3:
        print("selective moving")
        return True
    else:
        return False

def flip(n):
    print("flipping")
    return 4 + 4

def compare(x, y):
    print("comparing")
    return 7+7

# while True:
#     string = ''
#     line = input("Card> ")
#     while line != '':
#         string += line
#         line = input()
#     parser.parse(string)

parsing(open("test", "r"))



