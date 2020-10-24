 
                #ALANG
  * program : compound_statement DOT

    * compound_statement : START statement_list OUT

    * statement_list : statement
                   | statement SEMI statement_list

    * statement : compound_statement
              | assignment_statement
              | empty

    * assignment_statement : variable ASSIGN expr

    * empty :

    * expr: term ((PLUS | MINUS) term)*

    * term: factor ((MUL | DIV) factor)*

    * factor :<br> PLUS factor
           | MINUS factor
           | INTEGER
           | LPAREN expr RPAREN
           | variable
    * variable: ID

-----------------------------------------------------------------------------------
## Compount Statement:
It contains a list of 0 or n statement and compound_statements.
### Syntax:
START<br>
   ---------.<br>
    ---------.<br>
OUT

-> It must start with the KEYWORD 'START' and end with OUT
-> Every statement inside the compound statement must end with a full stop "."

