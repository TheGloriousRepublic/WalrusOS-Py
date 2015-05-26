from WaSh_AST import *
from WaSh_lexer import *
from WaSh_parser_combinators import *

def keyword(kw):
    return Reserved(kw, RESERVED)

name = Tag(NAME)
integer = Tag(INT) ^ (lambda i: int(i))
dec = Tag(DEC) ^ (lambda i: float(i))

def aexp_value():
    return (integer ^ (lambda i: IntExp(i))) | (dec ^ (lambda i: IntExp(i))) | (id  ^ (lambda v: VarExp(v)))
