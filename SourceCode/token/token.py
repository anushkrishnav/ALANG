
INTEGER, PLUS, EOF, MINUS = 'INTEGER', 'PLUS', 'EOF', 'MINUS'
POW, DIV, MUL, LPAR, RPAR = 'POW', 'DIV', 'MUL', 'LPAR', 'RPAR'


class Token(object):
    def __init__(self, type, value):
        """
        Token Object  with type and value               
        """
        self.type = type
        self.value = value

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
