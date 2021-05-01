import sys, os
sys.path.append(os.path.abspath("SOURCECODE"))
from token.token import Token
# from interpreter import main

INTEGER, PLUS, EOF, RPAR = 'INTEGER',  'PLUS', 'EOF', 'RPAR'
MINUS, POW, DIV, MUL, LPAR = 'MINUS', 'POW', 'DIV', 'MUL', 'LPAR'
OPERATORS = {'+': PLUS, '-': MINUS, '^': POW, '/': DIV, '*': MUL}
BRACKETS = {'(': LPAR, ')': RPAR}
ASSIGN, DOT, SEMI, ID = 'ASSIGN', 'DOT', 'SEMI', 'ID'
KEYWORDS = {
    'START': Token('START', 'START'),
    'STOP': Token('STOP', 'STOP'),
}


class Lexer(object):
    def __init__(self, text):
        # client string input,  e.g. "3 + 5",  "12 - 5",  etc
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]
    ######################
    # Lexer code         #
    ######################

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos > len(self.text)-1:
            return None
        else:
            return self.tect[peek_pos]

    def Error(self):
        raise ValueError('Invalid char ')

    def Advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def Skip_Whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.Advance()

    def _id(self):
        """Handle identifiers and reserved keywords"""
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.Advance()

        token = KEYWORDS.get(result, Token(ID, result))
        return token

    def Integer(self):
        """Return a (multidigit) Integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():

            result += self.current_char
            self.Advance()
        return int(result)

    def Get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.Skip_Whitespace()
                continue

            if self.current_char.isalpha():
                return self._id()

            if self.current_char == '=':
                self.Advance()
                self.Advance()
                return Token(ASSIGN, '=')

            if self.current_char == ';':
                self.Advance()
                return Token(SEMI, ';')

            if self.current_char == '.':
                self.Advance()
                return Token(DOT, '.')
            
            if self.current_char in BRACKETS.keys():
                token = Token(BRACKETS.get(self.current_char),
                              self.current_char)
                self.Advance()
                return token

            if self.current_char.isdigit():
                return Token(INTEGER,  self.Integer())

            if self.current_char in OPERATORS.keys():
                token = Token(OPERATORS.get(self.current_char),
                              self.current_char)
                self.Advance()
                return token
            self.Error()

        return Token(EOF,  None)
