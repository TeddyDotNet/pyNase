import lex
import re

tokens = (
    'DELIMITER_SYMBOL',
    'EOF_SYMBOL',
    'INT_TYPE_SYMBOL',
    'COMMA_SYMBOL',
    'ASSIGN_SYMBOL',
    'MINUS_SYMBOL',
    'PLUS_SYMBOL',
    'TIMES_SYMBOL',
    'DIVIDE_SYMBOL',
    'MODULO_SYMBOL',
    'OR_SYMBOL',
    'AND_SYMBOL',
    'OPEN_PARAENTHESIS_SYMBOL',
    'CLOSE_PARAENTHESIS_SYMBOL',
    'INLINE_IF_SYMBOL',
    'INLINE_FI_SYMBOL',
    'INLINE_THEN_SYMBOL',
    'INLINE_ELSE_SYMBOL',
    'LT_SYMBOL',
    'LE_SYMBOL',
    'EQ_SYMBOL',
    'GE_SYMBOL',
    'GT_SYMBOL',
    'NE_SYMBOL',
    'READ_SYMBOL',
    'WRITE_SYMBOL',
    'IDENTIFIER',
    'ANY_DIGIT'
    )

reserved_words = {
    'INTEGER' : 'INTEGER',
    'OR' : 'OR',
    'AND' : 'AND',
    'READ' : 'READ',
    'WRITE' : 'WRITE',
    'IIF' : 'IIF',
    'FII' : 'FII'
}

t_ignore = ' \t\n'
t_DELIMITER_SYMBOL = r";"
t_EOF_SYMBOL = r"\z"
t_COMMA_SYMBOL = r","
t_ASSIGN_SYMBOL = r":="
t_MINUS_SYMBOL = r"-"
t_PLUS_SYMBOL = r"\+"
t_TIMES_SYMBOL = r"\*"
t_DIVIDE_SYMBOL = r"/"
t_MODULO_SYMBOL = r"%"
t_OPEN_PARAENTHESIS_SYMBOL = r"\("
t_CLOSE_PARAENTHESIS_SYMBOL = r"\)"
t_INLINE_IF_SYMBOL = r"IIF"
t_INLINE_FI_SYMBOL = r"FII"
t_INLINE_THEN_SYMBOL = r"\?"
t_INLINE_ELSE_SYMBOL = r":"
t_LT_SYMBOL = r"<"
t_LE_SYMBOL = r"<="
t_EQ_SYMBOL = r"="
t_GE_SYMBOL = r">="
t_GT_SYMBOL = r">"
t_NE_SYMBOL = r"<>"
t_READ_SYMBOL = r"READ"
t_WRITE_SYMBOL = r"WRITE"
t_INT_TYPE_SYMBOL = r"INTEGER"
t_OR_SYMBOL = r"OR"
t_AND_SYMBOL = r"AND"


def t_error(t):
    print "Line %d." % (t.lineno,) + "",
    if t.value[0] == '"':
        print "Unterminated string literal."
        if t.value.count('\n') > 0:
            t.skip(t.value.index('\n'))
    elif t.value[0:2] == '/*':
        print "Unterminated comment."
    else:
        print "Illegal character '%s'" % t.value[0]
        t.skip(1)

def t_IDENTIFIER(t):
    r"[a-z][\w]*"
    if reserved_words.has_key(t.value):
        pass
    return t

def t_ANY_DIGIT(t):
    r"[0-9]"
    return t

# create lexer
lex.lex() 

def lexTheCode(code):

    lex.input(code)

    # DEBUG OUTPUT
    print "----------------"
    print "TOKENS:"
    print "----------------"
    while True:
         tok = lex.token()
         if not tok: break
         print tok
