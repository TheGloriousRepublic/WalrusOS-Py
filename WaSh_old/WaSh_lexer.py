import re
RESERVED = 'RESERVED'
STRING = 'STRING'
INT = 'INT'
DEC = 'DEC'
NAME = 'NAME'

tags = {
    (r'("[^"]*"|\'[^\']*\')',   STRING),
    (r'(\s|\t|\n)',             None),
    (r';',                      RESERVED),
    (r'if',                     RESERVED),
    (r'then',                   RESERVED),
    (r'while',                  RESERVED),
    (r'do',                     RESERVED),
    (r'==',                     RESERVED),
    (r':=',                     RESERVED),
    (r'=',                      RESERVED),
    (r'\+',                     RESERVED),
    (r'-',                      RESERVED),
    (r'\*',                     RESERVED),
    (r'/',                      RESERVED),
    (r'\^',                     RESERVED),
    (r'\(',                     RESERVED),
    (r'\)',                     RESERVED),
    (r'TRUE',                   RESERVED),
    (r'FALSE',                  RESERVED),
    (r'nand',                   RESERVED),
    (r'nor',                    RESERVED),
    (r'and',                    RESERVED),
    (r'xor',                    RESERVED),
    (r'xnor',                   RESERVED),
    (r'or',                     RESERVED),
    (r'[0-9]+\.[0-9]+',         DEC),
    (r'[0-9]+',                 INT),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', NAME),
    (r'\.',                     RESERVED),
    }

def lex(com):
    i = 0
    tokens = []
    while i < len(com):
        match = None
        for x in tags:
            pattern, tag = x
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
