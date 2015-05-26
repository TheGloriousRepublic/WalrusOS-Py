import filesys
import processes
import WaSh_lexer
import WaSh_parser

class shell:
    def lex(self, com):
        WASH_lexer.lex(com)

    def parse(self, tok):
        WASH_parser.parse(tok)
    
	def AST(self):
		pass
	
    def do(self, com):
        self.commands={'echo'}
        return self.execute(self.parse(self.lex(com)))

    def execute(self, com, inputs):
        for x in [com]:
            if x == 'echo':
                return ' '.join(inputs[0:])
            elif x == 'kill':
                pass
