# C Compiler

compiler written in Haskell

* Following this series of tutorials - https://norasandler.com/2017/11/29/Write-a-Compiler.html

## Progress
------------

### Lexing

* lex.py
* scanner/tokenizer, breaks up source code into a list of tokens. A token is the smallest unit the parser can understand.


### Parsing

* Tokens -> AST (Abstract syntax tree)
* Root of AST will be the entire program and each node will have children representing its constituent parts.

#### Example:

``````````````````
   if (a < b){
       c = 2;
       return c;
    } else {
      c = 3;
    }
``````````````````

* the condition (a < b)
* the if body (c = 2; return c;)
* the else body ( c = 3)

##### Further Breakdown
* Condition - binary operation with two children (a, b)
* Assignment (c = 2) has two children, (c, 2)
<img src="https://norasandler.com/assets/AST.svg">
 
