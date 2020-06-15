from Token import Token

# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER,PLUS,EOF,MINUS,POW,DIV,MUL = 'INTEGER', 'PLUS', 'EOF','MINUS','POW','DIV','MUL'
OPERATORS={'+':PLUS,'-':MINUS,'**' :POW,'/':DIV,'*':MUL}

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3 + 5", "12 - 5", etc
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]
##########################################################
    # Lexer code                                             #
    ##########################################################
    

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():

            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char in OPERATORS.keys():
                token=Token(OPERATORS.get(self.current_char),self.current_char)
                self.advance()
                return token
            self.error()

        return Token(EOF, None)
 ##########################################################
    # Parser / Interpreter code                              
    ##########################################################
    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
    def calc(self,left,value,right):
        if value=='-':
            result = left - right
            return result

        if value=='+':
            result = left + right
            return result
        
        if value=='*':
            result = left * right
            return result
        
        if value=='/':
            if right==0:
                raise ValueError("You cannot divide a number by 0")
            result = left / right
            return result
        
        if value=='**':
            result = left ** right
            return result
    def term(self):
        """Return an INTEGER token value"""
        token=self.current_token
        self.eat(INTEGER)
        return token.value
    """------------------Parser / Interpreter ---------------------------"""
    def expr(self):
        #art expression parser/interpreter
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()
        result=self.term()
        while self.current_token.type in OPERATORS.values():
            token=self.current_token
            if self.current_token.type in OPERATORS.values():
                op=self.current_token.value
                self.eat(self.current_token.type)
                term3=self.term()
                result=self.calc(result,op,term3)

        # we expect the current token to be an integer
        # after the above call the self.current_token is set to
        # EOF token

        # at this point either the INTEGER PLUS INTEGER or
        # the INTEGER MINUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding or subtracting two integers,
        # thus effectively interpreting client input
        return result


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('>>> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text.strip())
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()

