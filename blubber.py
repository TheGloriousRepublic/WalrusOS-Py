class stackError(Exception):
    pass

class inputError(Exception):
    pass

class stack(list):
    def push(self, item):
        self.append(item)
        
    def pop(self):
        if len(self)>0:
            e=self[-1]
            del self[-1]
            return e
        else:
            raise(stackError, 'To pop an item from a stack you must have an item on the stack')

    def empty(self):
        del self[0:]
    
    def dup(self):
        e=self.pop()
        self.push(e)
        self.push(e)

    def swap(self):
        a=self.pop()
        b=self.pop()
        self.push(a)
        self.push(b)

    def over(self):
        a=self.pop()
        b=self.pop()
        self.push(b)
        self.push(a)
        self.push(b)

    def rotate(self):
        a=self.pop()
        b=self.pop()
        c=self.pop()
        self.push(b)
        self.push(c)
        self.push(a)
        
    def peek(self):
        e=self.pop()
        self.push(e)
        return e

    

s=stack()

def parse(script):
    return script.split(' ')
    
def run(script):
    script=parse(script)
    x=0
    for x in script:
        c=x.upper()

        if c.isdigit():
            s.push(int(c))
        else:
            if c == 'SAY':
                print(s.pop())

            elif c == 'SAS':
                o=''
                for y in s:
                    o=str(y)+' '+o
                print(o)

            elif c == 'CLR':
                s.empty()
                
            elif c == 'POP':
                s.pop()
                
            elif c == 'DUP':
                s.dup()

            elif c == 'SWP':
                s.swap()

            elif c == 'OVER':
                s.over()
                
            elif c == 'ADD':
                a=s.pop()
                b=s.pop()
                c=a+b
                s.push(a)
                s.push(b)
                s.push(c)
                
            elif c == 'SUB':
                a=s.pop()
                b=s.pop()
                c=a-b
                s.push(a)
                s.push(b)
                s.push(c)
                
            elif c == 'MLT':
                a=s.pop()
                b=s.pop()
                c=a*b
                s.push(a)
                s.push(b)
                s.push(c)
                
            elif c == 'DIV':
                a=s.pop()
                b=s.pop()
                c=a/b
                s.push(a)
                s.push(b)
                s.push(c)
                
            elif c == 'MOD':
                a=s.pop()
                b=s.pop()
                c=a%b
                s.push(a)
                s.push(b)
                s.push(c)
                
            elif c == 'EXP':
                a=s.pop()
                b=s.pop()
                c=a**b
                s.push(a)
                s.push(b)
                s.push(c)
                
            else:
                raise(inputError, 'Input was neither a command nor an integer')

#while True:
#    run(raw_input('-->'))
while True:
    d=open(raw_input('file: ')).read()
    run(d)
