from Token import Token
from Lexer import Lexer
INTEGER,PLUS,EOF,MINUS,POW,DIV,MUL,LPAR,RPAR = 'INTEGER', 'PLUS', 'EOF','MINUS','POW','DIV','MUL', 'LPAR' , 'RPAR'
OPERATORS={'+':PLUS,'-':MINUS,'^' :POW,'/':DIV,'*':MUL}

class AST(object):
    pass

class BinOP(AST):
    def __init__(self,left,op,right):
        self.left=left
        self.token=self.op=op
        self.right=right
class Num(AST):
    def __init__(self,Token):
        self.Token=Token
        self.value=Token.value
class NodeVisitor(object):
    def visit(self,node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))
class UnaryOP(AST):
    def __init__(self,op,expr):
        self.token=self.op=op
        self.expr=expr
