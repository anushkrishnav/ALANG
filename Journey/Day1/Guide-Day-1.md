I finnaly felt I was a prepared to take up a very challening task .Take a guess .
Yes finnaly a worthy challange our battles will be legendary.
I have decided to build a ...*Drum Roll*... Interpreter in Python .
I am a begginer in respect to all aspects will i be able to do it or will i quit defeatd i dont know .
I have given a look over how compiler and Interpreter works at article at geek for geek , and inside pvm
First thing first what is interpreter or compiler?
    Simply if a translator translates a source program into machine language, it is a compiler. If a translator processes and executes the source program without translating it into machine language first, it is an interpreter.
With the gained knowledge I decided to code a simple interpreter for a basic expression of adding 2 single digit Integers .

To achieve this :
declare
INTEGER,PLUS,EOF,MINUS,POW,DIV,MUL as global variables which we will use as the type for the character we tokenise

I need to get input
create a interpreter object and pass the input
set the input as an attribute
set a variable to 0 which we can use as a pointer to access the characters in the input.
We first need to do Lexical analysis the method get_next_token of the Interpreter class will be used for this purpose.
    We need to break the input into stream of Tokens
    A Token is an object which has value and a type 
    1)The method first checks whether the character is a digit and if so, it increments pos and returns a token instance with the type INTEGER and the value set to the integer value of the string 
    2)The pos now points to the OPERATOR character in the text. The next time you call the method, it tests if a character at the position pos is a digit and then it tests if the character is a plus sign, which it is. As a result the method increments pos and returns a newly created token with the type  and value OPERATOR:
    3)The pos now points to the next character . When you call the get_next_token method again the method checks if it’s a digit, which it is, so it increments pos and returns a new INTEGER token with the value of the token set to integer's value:
    4)our expression has only 3 characters for now now pos is 4 which is past the string lenght.
    the get_next_token method returns the EOF token every time you call it

Interpreter Now has access to the stream of tokens made from the input characters
Interpreter needs to find the structure in the flat stream of tokens it gets from the lexer get_next_token.
Interpreter expects to find the following structure in that stream: INTEGER -> OPERATOR -> INTEGER. 
The method responsible for finding and interpreting that structure is Start.
This method verifies that the sequence of tokens does indeed correspond to the expected sequence of tokens, i.e INTEGER -> Operator -> INTEGER.
 After it’s successfully confirmed the structure, it generates the result by operationg on  the value of the token on the left side of the OPERATOR and the right side of the OPERATOR, thus successfully interpreting the arithmetic expression we passed to the interpreter.


