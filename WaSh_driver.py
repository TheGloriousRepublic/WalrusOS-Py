import WaSh

sh = WaSh.shell()
m=raw_input('mode>').upper()

while True:
    if m =='REPL':
        print(sh.do(raw_input('>'))) #REPL
    elif m == 'LEX':
        print(sh.lex(raw_input('>'))) #lexer driver
    elif m == 'PARSE':
        print(sh.parse(sh.lex(raw_input('>'))))
    elif m == 'AST':
        print(sh.AST)
