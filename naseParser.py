import yacc
import naseLexer          

tokens = naseLexer.tokens   

class ParseError(Exception):
    "Exception raised whenever a parsing error occurs."
    pass

def p_program(p):
	'''program : statementSequence'''
	print "program:"

def p_statementSequence(p):
	'''statementSequence : statement partialStatementSequence'''
	print "statementSequence:"

def p_partialStatementSequence(p):
	'''partialStatementSequence : statement partialStatementSequence
								  | empty'''

def p_statement(p):
	'''statement : partialStatement DELIMITER_SYMBOL'''
	print "statement:"

def p_partialStatement(p):
	'''partialStatement : declaration
						| assignment
						| read
						| write
						| empty'''

def p_read(p):
	'''read : READ_SYMBOL IDENTIFIER'''
	print ("READ: %s %s" %(p[1],p[2]))

def p_write(p):
	'''write : WRITE_SYMBOL IDENTIFIER'''
	print ("WRITE: %s" %p[2])

def p_declaration(p):
	'''declaration : typeName IDENTIFIER partialDeclaration'''
	print "declaration %s" %p[2]


def p_partialDeclaration(p):
	'''partialDeclaration : COMMA_SYMBOL IDENTIFIER partialDeclaration
						  | empty'''


def p_typeName(p):
	'''typeName : INT_TYPE_SYMBOL'''
	print ("typeName: %s" %(p[1]))

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN_SYMBOL intExpr'''
    print ("assignment: %s %s %s" %(p[1],p[2],p[3]))

def p_intExpr(p):
	'''intExpr  : MINUS_SYMBOL intTerm partialIntExpr
				| intTerm partialIntExpr'''
	print ("intExpr: %s %s" %(p[1],p[2]))

def p_partialIntExpr(p):
	'''partialIntExpr : addOp intTerm partialIntExpr
					  | empty'''

def p_addOp(p):
	'''addOp : PLUS_SYMBOL 
			 | MINUS_SYMBOL'''
	print ("addOp: %s" %(p[1]))

def p_intTerm(p):
	'''intTerm : intFactor 
			   | intFactor partialIntTerm'''
	print ("intTerm: %s" %(p[1]))

def p_partialIntTerm(p):
	'''partialIntTerm : multOp intFactor partialIntTerm
					  | empty'''

def p_intFactor(p):
	'''intFactor : integer 
				 | IDENTIFIER
				 | OPEN_PARAENTHESIS_SYMBOL intExpr CLOSE_PARAENTHESIS_SYMBOL 
				 | inlineIfStatement'''
	print ("intFactor: %s" %(p[1]))

def p_multOp(p):
	'''multOp : TIMES_SYMBOL
			  | DIVIDE_SYMBOL
			  | MODULO_SYMBOL'''
	print ("multOp: %s" %(p[1]))

def p_inlineIfStatement(p):
	'''inlineIfStatement : INLINE_IF_SYMBOL boolExpr INLINE_THEN_SYMBOL intExpr INLINE_ELSE_SYMBOL intExpr INLINE_FI_SYMBOL'''
	print ("inlineIfStatement: ")

def p_partialBoolExpr(p):
	'''partialBoolExpr : boolOp intExpr relationOp intExpr partialBoolExpr
						 | empty'''

def p_boolExpr(p):
	'''boolExpr : intExpr relationOp intExpr partialBoolExpr'''
	print ("boolExpr: ")

def p_boolOp(p):
	'''boolOp : AND_SYMBOL
			  | OR_SYMBOL'''
	print ("boolOp: %s" %(p[1]))

def p_relationOp(p):
	'''relationOp : LT_SYMBOL
				  | LE_SYMBOL
				  | EQ_SYMBOL
				  | GE_SYMBOL
				  | GT_SYMBOL
				  | NE_SYMBOL'''
	print ("relationOp: %s" %(p[1]))

def p_integer(p):
	'''integer : ANY_DIGIT digits'''
	print ("integer: %s" %(p[0]))

def p_digits(p):
	'''digits : ANY_DIGIT digits
			 | empty'''


def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print "You've got a syntax error somewhere in your code."
    print "It could be around line %d." % t.lineno
    print "Good luck finding it."
    raise ParseError()

yacc.yacc() 

def parseCode(code):
	print "----------------"
	print "PARSING CODE:"
	print "----------------"
	return yacc.parse(code)
