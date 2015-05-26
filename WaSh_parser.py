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

def process_group(parsed):
    ((_, p), _) = parsed
    return p

def aexp_group():
    return keyword('(') + Lazy(aexp) + keyword(')') ^ process_group

def aexp_term():
    return aexp_value() | aexp_group()

def process_biexp(op):
    return lambda l, r: BiExp(op, l, r)
