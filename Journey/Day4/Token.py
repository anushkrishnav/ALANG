# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER,PLUS,EOF,MINUS,POW,DIV,MUL,LPAR,RPAR = 'INTEGER', 'PLUS', 'EOF','MINUS','POW','DIV','MUL', 'LPAR' , 'RPAR'

class Token(object):
    def __init__(self,type,value):
        #token type: INTEGER,PLUS,EOF
        self.type=type
        #token value:0,1,2,3,4,5,6,7,8,9,operators,or None
        self.value=value
    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type},{value})'.format(
            type=self.type,
            value=repr(self.value)
        )
    def __repr__(self):
        return self.__str__()
    

