import sys, os
sys.path.append(os.path.abspath("SOURCECODE"))

INTEGER, PLUS, EOF, RPAR = 'INTEGER',  'PLUS', 'EOF', 'RPAR'
MINUS, POW, DIV, MUL, LPAR = 'MINUS', 'POW', 'DIV', 'MUL', 'LPAR'
OPERATORS = {'+': PLUS, '-': MINUS, '^': POW, '/': DIV, '*': MUL}


class AST(object):
    pass


class BinOP(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class UnaryOP(AST):

    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class NodeVisitor(object):

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))
