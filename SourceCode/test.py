# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER,PLUS,EOF,MINUS,POW,DIV,MUL = 'INTEGER', 'PLUS', 'EOF','MINUS','POW','DIV','MUL'

OPERATORS={'+':PLUS,'-':MINUS,'**' :POW,'/':DIV,'*':MUL}

class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS, or EOF
        self.type = type
        # token value: non-negative integer value, '+', '-', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()



