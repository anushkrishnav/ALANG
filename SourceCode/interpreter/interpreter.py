import sys, os
sys.path.append(os.path.abspath("SOURCECODE"))

# from Token import Token.
from abstract_syntax_tree.AST  import NodeVisitor, Num, BinOP, UnaryOP

# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, EOF, RPAR = 'INTEGER',  'PLUS', 'EOF', 'RPAR'
MINUS, POW, DIV, MUL, LPAR = 'MINUS', 'POW', 'DIV', 'MUL', 'LPAR'
OPERATORS = {'+': PLUS, '-': MINUS, '^': POW, '/': DIV, '*': MUL}


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_UnaryOP(self, node):
        op = node.op.type
        if op == PLUS:
            return +self.visit(node.expr)
        if op == MINUS:
            return -self.visit(node.expr)

    def visit_BinOP(self, node):
        if node.op.value == '-':
            result = self.visit(node.left) - self.visit(node.right)
            return result
        if node.op.value == '+':
            result = self.visit(node.left) + self.visit(node.right)
            return result
        if node.op.value == '*':
            result = self.visit(node.left) * self.visit(node.right)
            return result
        if node.op.value == '/':
            if self.visit(node.right) == 0:
                raise ValueError("You cannot divide a number by 0")
            result = self.visit(node.left) / self.visit(node.right)
            return result
        if node.op.value == '^':
            result = self.visit(node.left)**self.visit(node. righ)
            return result

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''
        return self.visit(tree)

