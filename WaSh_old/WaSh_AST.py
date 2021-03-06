class Equality: #Test if two things are the same
    def __eq__(self, other):
        return(isinstance(other, self.__class__) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return(not self.__eq__(other))

#Arithmetical Expressions
class IntExp(Equality): #Integer
    def __init__(self, i):
        self.i=i
    
    def __repr__(self):
        return('IntExp('+str(self.i)+')')

class StrExp(Equality): #String Expressions
    def __init__(self, s):
        self.s = s
    
    def __repr__(self):
        return('Exp('+self.s+')')
    
class VarExp(Equality): #Variable
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return('VarExp('+self.name+')')
    
class BiExp(Equality): #Binary expression (e.g. 2+2)
    def __init__(self, op, l, r):
        self.op = op
        self.left = l
        self.right = r
    
    def __repr__(self):
        return('BiExp('+str(self.op)+', '+str(self.left)+', '+str(self.right)+')')

#Boolean Expressions
class RBExp(Equality):
    def __init__(self, b):
        self.b = b
    
    def __repr__(self):
        return('RBExp('+self.b+')')

class RelopBExp(Equality):
    def __init__(self, op, l, r):
        self.op = op
        self.left = l
        self.right = r
    
    def __repr__(self):
        return('BiExp('+self.op+', '+self.left+', '+self.right+')')

class AndBExp(Equality):
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __repr__(self):
        return('AndBExp('+self.left+', '+self.right+')')

class NandBExp(Equality):
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __repr__(self):
        return('NandBExp('+self.left+', '+self.right+')')

class OrBExp(Equality):
    def __init__(self, l, r):
        self.left = l
        self.right = r
    
    def __repr__(self):
        return('OrBExp('+self.left+', '+self.right+')')

class NorBExp(Equality):
    def __init__(self, l, r):
        self.left = l
        self.right = r
    
    def __repr__(self):
        return('NorBExp('+self.left+', '+self.right+')')

class XorBExp(Equality):
    def __init__(self, l, r):
        self.left = l
        self.right = r
    
    def __repr__(self):
        return('XorBExp('+self.left+', '+self.right+')')
    
class XnorBExp(Equality):
    def __init__(self, l, r):
        self.left = l
        self.right = r
    
    def __repr__(self):
        return('XnorBExp('+self.left+', '+self.right+')')

class NotBExp(Equality):
    def __init__(self, e):
        self.exp = e
    
    def __repr__(self):
        return('NotBExp('+self.exp+')')
    
#Statements
class AssignStatement(Equality):
    def __init__(self, name, e):
         self.name = name
         self.exp = e
     
    def __repr__(self):
        return('AssignStatement('+self.name+', '+str(self.exp)+')')

    def eval(self, env):
        value = self.aexp.eval(env)
        env[self.name] = value

class CompoundStatement(Equality):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def __repr__(self):
        return('CompoundStatement('+self.first+', '+self.second+')')

    def eval(self, env):
        self.first.eval(env)
        self.second.eval(env)
    
class IfStatement(Equality):
    def __init__(self, condition, true_stmt, false_stmt):
        self.condition = condition
        self.ontrue = true_stmt
        self.onfalse = false_stmt

    def __repr__(self):
        return('IfStatement('+condition+', '+self.ontrue+', '+self.onfalse+')')

    def eval(self, env):
        condition_value = self.condition.eval(env)
        if condition_value:
            self.true_stmt.eval(env)
        else:
            if self.false_stmt:
                self.false_stmt.eval(env)

class WhileStatement(Equality):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    
    def __repr__(self):
        return('WhileStatement('+self.condition+', '+self.body+')')

    def eval(self, env):
        condition_value = self.condition.eval(env)
        while condition_value:
            self.body.eval(env)
            condition_value = self.condition.eval(env)
