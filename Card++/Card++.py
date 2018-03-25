import ply.lex as lex
import ply.yacc as yacc

# All lex rules

# List of tokens
tokens = (

)

# Build the lexer
lexer = lex.lex()

# All parse rules

# Build the parser
parser = yacc.yacc()
