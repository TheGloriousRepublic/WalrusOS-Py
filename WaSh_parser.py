from WaSh_AST import *
from WaSh_lexer import *
from WaSh_parser_combinators import *

def keyword(kw):
    return Reserved(kw, RESERVED)

name = Tag(NAME)
integer = Tag(INT) ^ (lambda i: int(i))
dec = Tag(DEC) ^ (lambda i: float(i))

def aexp_value():
    return (integer ^ (lambda i: IntExp(i))) | (dec ^ (lambda i: IntExp(i))) | (name  ^ (lambda v: VarExp(v)))

def process_group(parsed):
    ((_, p), _) = parsed
    return p

def aexp_group():
    return keyword('(') + Lazy(aexp) + keyword(')') ^ process_group

def aexp_term():
    return aexp_value() | aexp_group()

def process_BinExp(op):
    return lambda l, r: BiExp(op, l, r)

def anyop(ops):
    op_parsers = [keyword(op) for op in ops]
    parser = reduce(lambda l, r: l | r, op_parsers)
    return parser

aexp_precedence_levels = [
    ['^'],
    ['*', '/'],
    ['+', '-'],
]

def precedence(value_parser, precedence_levels, combine):
    def op_parser(precedence_level):
        return anyop(precedence_level) ^ combine
    parser = value_parser * op_parser(precedence_levels[0])
    for precedence_level in precedence_levels[1:]:
        parser = parser * op_parser(precedence_level)
    return parser

def aexp():
    return precedence(aexp_term(), aexp_precedence_levels, process_BinExp)

#Booleans
def process_relop(parsed):
    ((left, op), right) = parsed
    return RelopBexp(op, left, right)

def bexp_relop():
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return aexp() + anyop(relops) + aexp() ^ process_relop

def bexp_not():
    return keyword('not') + Lazy(bexp_term) ^ (lambda parsed: NotBexp(parsed[1]))

def bexp_group():
    return keyword('(') + Lazy(bexp) + keyword(')') ^ process_group

def bexp_term():
    return bexp_not() | bexp_relop() | bexp_group()

bexp_precedence_levels = [
    ['and', 'nand'],
    ['or', 'nor'],
    ['xor', 'xnor']
]

def process_logic(op):
    if op == 'and':
        return lambda l, r: AndBExp(l, r)
    elif op == 'nand':
        return lambda l, r: NandBExp(l, r)
    elif op == 'or':
        return lambda l, r: OrBExp(l, r)
    elif op == 'nor':
        return lambda l, r: NorBExp(l, r)
    elif op == 'xor':
        return lambda l, r: XorBExp(l, r)
    elif op == 'xnor':
        return lambda l, r: XnorBExp(l, r)
    else:
        raise RuntimeError('unknown logic operator: ' + op)

def bexp():
    return precedence(bexp_term(),
                      bexp_precedence_levels,
                      process_logic)

def assign_stmt():
    def process(parsed):
        ((name, _), exp) = parsed
        return AssignStatement(name, exp)
    return name + keyword(':=') + aexp() ^ process

def stmt_list():
    separator = keyword(';') ^ (lambda x: lambda l, r: CompoundStatement(l, r))
    return Exp(stmt(), separator)

def if_stmt():
    def process(parsed):
        (((((_, condition), _), true_stmt), false_parsed), _) = parsed
        if false_parsed:
            (_, false_stmt) = false_parsed
        else:
            false_stmt = None
        return IfStatement(condition, true_stmt, false_stmt)
    return keyword('if') + bexp() + keyword('then') + Lazy(stmt_list) + Opt(keyword('else') + Lazy(stmt_list)) + keyword('end') ^ process

def while_stmt():
    def process(parsed):
        ((((_, condition), _), body), _) = parsed
        return WhileStatement(condition, body)
    return keyword('while') + bexp() + keyword('do') + Lazy(stmt_list) + keyword('end') ^ process

def stmt():
    return assign_stmt() | if_stmt() | while_stmt()

def parser():
    print stmt_list()
    #print Phrase(stmt_list())
    #return Phrase(stmt_list())
    return stmt_list()

def WaSh_parse(tokens):
    ast = parser()(tokens, 0)
    return ast
