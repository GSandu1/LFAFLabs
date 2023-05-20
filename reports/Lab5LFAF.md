# Parser & Building an Abstract Syntax Tree

## Course: Formal Languages & Finite Automata  
## Author: Gazea Sandu




## Theory

Parsing is the process of extracting syntactical meaning from a piece of text, such as a programming language expression. It involves analyzing the text and creating a hierarchical structure that represents the relationships between the different components of the text. This structure is often referred to as a parse tree.

In addition to the parse tree, another useful representation of the text's structure is the Abstract Syntax Tree (AST). The AST captures the essential elements of the text while abstracting away unnecessary details. It organizes the components of the text into layers of abstraction that correspond to the constructs or entities present in the original text.

The AST is particularly valuable in the analysis of programs and various stages of compilation. It provides a concise and structured representation of the program's syntax, which can be used for tasks like semantic analysis, optimization, and code generation.

Overall, parsing and the creation of an AST play crucial roles in understanding and processing text, especially in the context of programming languages and compilation processes.


## Objectives

1. Get familiar with parsing, what it is and how it can be programmed [^1].
2. Get familiar with the concept of AST [^2].
3. In addition to what has been done in the 3rd lab work, do the following:
    1. In case you didn't have a type that denotes the possible types of tokens, you need to:
        1. Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens.
        2. Please use regular expressions to identify the type of the token.
    2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    3. Implement a simple parser program that could extract the syntactic information from the input text.


## Implementation description

### Parser Class

The `Parser` class is used to parse and analyze a sequence of tokens. Its `__init__` method initializes the class instance by setting the provided `tokens` as the input tokens and setting the current token to `None`. The `next()` method is then called to set the first token as the current token.
```python
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next()
```

### `next` method

This method advances the current token to the next token in the list by removing the first token from the `tokens` list. If there are no more tokens, it sets the `current_token` to `None`.
```python
    def next(self):
        self.current_token = self.tokens.pop(0) if self.tokens else None
```

### `expression` method
This function handles the parsing of an expression. It first looks for a `term` by calling the term() function. Then, it checks if there are any more tokens and if the current token is either a plus or minus operator. If it finds a plus operator, it knows that there is another term to add, so it advances to the next token and recursively calls the `term()` function to parse the next term. It keeps track of the intermediate result using the `expr` variable. If it finds a minus operator, it follows a similar process but with subtraction instead. Finally, it returns the fully parsed expression.
```python
    def expression(self):
        print('Parsing expression: term')
        expr = self.term()
        while self.current_token and self.current_token.type in ('PLUS', 'MINUS'):
            if self.current_token.type == 'PLUS':
                print('Parsing expression: add')
                self.next()
                expr = ('ADD', expr, self.term())
            elif self.current_token.type == 'MINUS':
                print('Parsing expression: subtract')
                self.next()
                expr = ('SUB', expr, self.term())
        return expr
    
```
### `term` method

This method handles the parsing of a term. It first calls the `factor()` method to parse the initial factor. Then, it enters a loop that continues as long as there are more tokens and the current token is either a multiplication or division operator. Inside the loop, it checks the type of the current token and performs the corresponding operation (multiplication or division) by calling the `next()` method to advance to the next token and recursively calling the `factor()` method to parse the next factor. The result of each operation is stored in the `term` variable. Finally, it returns the parsed term.
```python
    def term(self):
        print('Parsing term: factor')
        term = self.factor()
        while self.current_token and self.current_token.type in ('TIMES', 'DIVIDE'):
            if self.current_token.type == 'TIMES':
                print('Parsing term: multiply')
                self.next()
                term = ('MUL', term, self.factor())
            elif self.current_token.type == 'DIVIDE':
                print('Parsing term: divide')
                self.next()
                term = ('DIV', term, self.factor())
        return term

```

### `factor` method

This method handles the parsing of a factor. It checks the type of the current token and performs the corresponding action. If the current token is a number, it retrieves the value of the number, advances to the next token, and returns a tuple representing the number. If the current token is a left parenthesis, it advances to the next token and recursively calls the `expression()` method to parse the expression within the parentheses. After that, it checks if the current token is a right parenthesis. If not, it raises an exception. Finally, it advances to the next token and returns the parsed factor.
```python
    def factor(self):
        if self.current_token.type == 'NUMBER':
            value = self.current_token.value
            print('Parsing factor: number {}'.format(value))
            self.next()
            return ('NUM', value)
        elif self.current_token.type == 'LPAREN':
            print('Parsing factor: expression')
            self.next()
            value = self.expression()
            if self.current_token.type != 'RPAREN':
                raise Exception('Expected )')
            self.next()
            return value
        raise Exception('Unexpected token')
```

### Interpreter
The `Interpreter` class evaluates an Abstract Syntax Tree (AST) by interpreting its nodes recursively. It supports arithmetic operations like addition, subtraction, multiplication, and division. The `interpret` method takes a node and performs the corresponding operation based on the node type. If the node type is `'NUM'`, it returns the numeric value. Otherwise, it recursively interprets the left and right sub-trees and performs the operation using the interpreted values. If an invalid node type is encountered, it raises a `ValueError`. The `Interprete`r class enables the evaluation of arithmetic expressions represented by the AST.
```python
    class Interpreter:
        def __init__(self):
            self.variables = {}

        def interpret(self, tree):
            node_type = tree[0]

            if node_type == 'NUM':
                return float(tree[1])

            if node_type == 'ADD':
                left_value = self.interpret(tree[1])
                right_value = self.interpret(tree[2])
                return left_value + right_value

            if node_type == 'SUB':
                left_value = self.interpret(tree[1])
                right_value = self.interpret(tree[2])
                return left_value - right_value

            if node_type == 'MUL':
                left_value = self.interpret(tree[1])
                right_value = self.interpret(tree[2])
                return left_value * right_value

            if node_type == 'DIV':
                left_value = self.interpret(tree[1])
                right_value = self.interpret(tree[2])
                return left_value / right_value

            raise ValueError(f"Invalid node type: {node_type}")

```

```
# Input:
```
2 + 3 * (4 - 1)
```
# Results:
```
Parsing expression...

Parsing expression: term

Parsing term: factor

Parsing factor: number 2

Parsing expression: add

Parsing term: factor

Parsing factor: number 3

Parsing term: multiply

Parsing factor: expression

Parsing expression: term

Parsing term: factor

Parsing factor: number 4

Parsing expression: subtract

Parsing term: factor

Parsing factor: number 1

Result of 2 + 3 * (4 - 1) is 11.0
```

# Conclusion

Parsers and interpreters are essential in programming languages and software development. Parsers break down code into smaller parts, while interpreters execute the parsed code. Abstract Syntax Trees (ASTs) provide a structured representation of code's syntactic structure, simplifying code manipulation and analysis. Understanding parsers, interpreters, and ASTs empowers developers to create languages, optimize code, and build innovative tools. They enhance productivity and play a vital role in software development.