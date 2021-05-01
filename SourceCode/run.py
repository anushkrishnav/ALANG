import sys, os
sys.path.append(os.path.abspath("SOURCECODE"))

from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

if __name__ == '__main__':
    def main():
        while True:
            try:
                # To run under Python3 replace 'raw_input' call
                # with 'input'
                text = input('alng >>')
            except EOFError:
                break
            if not text:
                continue
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            result = interpreter.interpret()
            print(result)
    main()
