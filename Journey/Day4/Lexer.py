from Token import Token
INTEGER,PLUS,EOF,MINUS,POW,DIV,MUL,LPAR,RPAR = 'INTEGER', 'PLUS', 'EOF','MINUS','POW','DIV','MUL', 'LPAR' , 'RPAR'
OPERATORS={'+':PLUS,'-':MINUS,'**' :POW,'/':DIV,'*':MUL}
class Lexer(object):
    def __init__(self,text):
                # client string input, e.g. "3 + 5", "12 - 5", etc
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]
    ######################
    # Lexer code         #
    ######################
    

    def Error(self):
        raise Exception('Invalid char ')

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

            if self.current_char.isdigit():
                return Token(INTEGER, self.Integer())

            if self.current_char in OPERATORS.keys():
                token=Token(OPERATORS.get(self.current_char),self.current_char)
                self.Advance()
                return token
            self.Error()

        return Token(EOF, None)
