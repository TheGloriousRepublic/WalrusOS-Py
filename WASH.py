import re
import filesys
import processes

class shell:
    def lex(self, com):
        RESERVED = 'RESERVED'
        STRING = 'STRING'
        INT = 'INT'
        DEC = 'DEC'
        NAME = 'NAME'
        
        self.tags = {
            (r'("[^"]*"|\'[^\']*\')',   STRING),
            (r'\+',                     RESERVED),
            (r'-',                      RESERVED),
            (r'\*',                     RESERVED),
            (r'/',                      RESERVED),
            (r'\^',                     RESERVED),
            (r'\(',                     RESERVED),
            (r'\)',                     RESERVED),
            (r'[0-9]+\.[0-9]+',         DEC),
            (r'[0-9]+',                 INT),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', NAME)
            }

        i = 0
        tokens = []
        while i < len(com):
            match = None
            for x in self.tags:
                pattern, tag = x
                print pattern
                r = re.compile(pattern)
                match = r.match(com, i)
                if match:
                    text = match.group(0)
                    if tag:
                        tokens.append((text, tag))
                    i = match.end(0)
                    break
            if match == None:
                raise ValueError('Invalid Character')
        return tokens
                

    def do(self, com):
        self.commands={'echo'}
        return self.execute(lex(com))

    def execute(self, com, inputs):
        for x in [com]:
            if x == 'echo':
                return ' '.join(inputs[0:])
            elif x == 'kill':
                pass
        
        

if __name__=='__main__':
    sh = shell()
    #while True:
    #    print(sh.do(raw_input('>'))) #REPL
    print(sh.lex(raw_input())) #lexer driver
