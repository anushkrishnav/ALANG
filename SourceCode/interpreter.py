from Token import Token

# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER,PLUS,EOF,MINUS,POW,DIV,MUL = 'INTEGER', 'PLUS', 'EOF','MINUS','POW','DIV','MUL'
OPERATORS={'+':PLUS,'-':MINUS,'**' :POW,'/':DIV,'*':MUL}

class Interpreter(object):
    def __init__(self, text):
        # client string input
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def calc(self,value,left,right):
        if value=='-':
            result = left.value - right.value
            return result

        if value=='+':
            result = left.value + right.value
            return result
        
        if value=='*':
            result = left.value * right.value
            return result
        
        if value=='/':
            result = left.value / right.value
            return result
        
        if value=='**':
            result = left.value ** right.value
            return result
    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
       
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        
        if current_char.isspace():
            self.pos +=1
            return self.get_next_token()

        if current_char in OPERATORS:
            token = Token(OPERATORS.get(current_char), current_char)
            self.pos += 1
            return token

        self.error()

    def remv(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "remv" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the current token to be a single-digit integer
        left = self.current_token
        self.remv(INTEGER)

        # we expect the current token to be a operator token
        op = self.current_token
        if op.value in OPERATORS:
            self.remv(OPERATORS.get(op.value))

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.remv(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token
        
        return self.calc(op.value,left,right)
        # at this point INTEGER Operator INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of opeartion two integers, thus
        # effectively interpreting client input
    


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('Al> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()