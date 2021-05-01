import sys, os
sys.path.append(os.path.abspath("SOURCECODE"))
from abstract_syntax_tree.AST import Num, BinOP, UnaryOP

INTEGER, PLUS, EOF, RPAR = 'INTEGER',  'PLUS', 'EOF', 'RPAR'
MINUS, POW, DIV, MUL, LPAR = 'MINUS', 'POW', 'DIV', 'MUL', 'LPAR'
OPERATORS = {'+': PLUS, '-': MINUS, '^': POW, '/': DIV, '*': MUL}


class Parser(object):
    def __init__(self, Lexer):
        self.Lexer = Lexer
        # current token instance
        self.current_token = self.Lexer.Get_next_token()

    ##############################
    # Parser / Interpreter code  #
    ##############################
    def Error(self):
        print('invalid syntax')

    def eat(self,  token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.Lexer.Get_next_token()
        else:
            self.Error()

    def factor(self):
        """Return an INTEGER token value"""
        res = self.current_token
        if res.type in (PLUS, MINUS):
            self.eat(res.type)
            node = UnaryOP(res, self.factor())
            return node
        if res.type == INTEGER:
            self.eat(INTEGER)
            return Num(res)
        elif res.type == LPAR:
            self.eat(LPAR)
            node = self.expr()
            self.eat(RPAR)
            return node

    def term(self):
        node = self.factor()
        # -------------------------OPERATOR PRESCEDENCE------------------#
        while self.current_token.type == POW:
            token = self.current_token
            if token.type in OPERATORS.values():
                self.eat(self.current_token.type)
            node = BinOP(left=node, op=token, right=self.factor())
        while self.current_token.type in (DIV, MUL):
            token = self.current_token
            if token.type in OPERATORS.values():
                self.eat(self.current_token.type)
            node = BinOP(left=node, op=token, right=self.factor())
        return node
    """------------------Parser / Interpreter ---------------------------"""

    def expr(self):
        # art expression parser/interpreter
        # set current token to the first token taken from the input
        node = self.term()
        while self.current_token.type in (PLUS,  MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)
            node = BinOP(left=node,  op=token,  right=self.term())

        while self.current_token.type in OPERATORS.values() and not None:
            token = self.current_token
            self.eat(self.current_token.type)
            node = BinOP(left=node, op=token, right=self.term())
        # we expect the current token to be an Integer
        # after the above call the self.current_token is set to
        # EOF token

        # at this point either the INTEGER PLUS INTEGER or
        # the INTEGER MINUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding or subtracting two integers,
        # thus effectively interpreting client input
        return node

    def parse(self):
        node = self.expr()
        if self.current_token.type != EOF:
            self.Error()
        return node
