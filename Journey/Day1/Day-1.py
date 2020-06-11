from Token import Token

# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER,PLUS,EOF,MINUS,POW,DIV,MUL = 'INTEGER', 'PLUS', 'EOF','MINUS','POW','DIV','MUL'
class Interpreter(object):
    def __init__(self, text):
        # client string input
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def Calc(self,value,left,right):
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
    def Error(self):
        raise Exception('Error parsing input')

    def GetNextToken(self):
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

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token
        if current_char == '*':
            token = Token(MUL, current_char)
            self.pos += 1
            return token
        if current_char == '/':
            token = Token(DIV, current_char)
            self.pos += 1
            return token     

        self.Error()

    def Remv(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "Remv" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.GetNextToken()
        else:
            self.Error()

    def Start(self):
        """Start -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.GetNextToken()

        # we expect the current token to be a single-digit integer
        left = self.current_token
        self.Remv(INTEGER)

        # we expect the current token to be a operator token
        op = self.current_token
        if op.value=='+':
            self.Remv(PLUS)
        if op.value=='-':
            self.Remv(MINUS)
        if op.value=='*':
            self.Remv(MUL)
        if op.value=='/':
            self.Remv(DIV)

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.Remv(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token
        
        return self.Calc(op.value,left,right)
        # at this point INTEGER Operator INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of opeartion two integers, thus
        # effectively interpreting client input
    


def Main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('code> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.Start()
        print(result)


if __name__ == '__main__':
    Main()