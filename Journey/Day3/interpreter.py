from Token import Token
from Lexer import Lexer
# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER,PLUS,EOF,MINUS,POW,DIV,MUL = 'INTEGER', 'PLUS', 'EOF','MINUS','POW','DIV','MUL'
OPERATORS={'+':PLUS,'-':MINUS,'**' :POW,'/':DIV,'*':MUL}
class Interpreter(object):
    def __init__(self,Lexer):
        self.Lexer=Lexer
        # current token instance
        self.current_token = self.Lexer.Get_next_token()
    
    ##############################
    # Parser / Interpreter code  #                  
    ##############################
    def Error(self):
        raise Exception('invalid syntax')
    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.Lexer.Get_next_token()
        else:
            self.Error()
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
        t1=self.term()
        while self.current_token.type in OPERATORS.values():
            token=self.current_token
            if token.type in OPERATORS.values():
                op=token.value
                self.eat(self.current_token.type)
                if self.current_token.value =='*':
                    op+='*'
                    self.eat(self.current_token.type)
                term3=self.term()
                result=self.calc(t1,op,term3)

        # we expect the current token to be an Integer
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
        lexer=Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()

