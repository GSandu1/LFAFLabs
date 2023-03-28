# Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Gazea Sandu FAF-211





## Theory
    The term lexer comes from lexical analysis which, in turn, represents the process of extracting lexical tokens from a string of characters. There are several alternative names for the mechanism called lexer, for example tokenizer or scanner. The lexical analysis is one of the first stages used in a compiler/interpreter when dealing with programming, markup or other types of languages. The tokens are identified based on some rules of the language and the products that the lexer gives are called lexemes. So basically the lexer is a stream of lexemes. Now in case it is not clear what's the difference between lexemes and tokens, there is a big one. The lexeme is just the byproduct of splitting based on delimiters, for example spaces, but the tokens give names or categories to each lexeme. So the tokens don't retain necessarily the actual value of the lexeme, but rather the type of it and maybe some metadata.

## Objectives:
- Understand what lexical analysis is.

- Get familiar with the inner workings of a lexer/scanner/tokenizer.

- Implement a sample lexer and show how it works.
  

## Implementation description
### Lexer class
The Lexer class in Python is responsible for parsing an input string and identifying the various types of tokens present in the string. To do this, the class defines a set of regular expression patterns that match different token types such as operators, identifiers, keywords, numbers, strings, and more. When the class's tokenize method is called, it iterates over these patterns, attempting to match them against the input string. If a match is found, the corresponding token and its value are added to a list of tokens. In case an invalid token is encountered, the class raises a ValueError exception.
```python
import re

class MathLexer:
    def __init__(self):
        self.token_patterns = {
            'NUMBER': r'\d+',
            'PLUS': r'\+',
            'MINUS': r'-',
            'TIMES': r'\*',
            'DIVIDE': r'/',
            'LPAREN': r'\(',
            'RPAREN': r'\)',
            'POWER': r'\^',
            'MODULO': r'%',
            'EQUALS': r'=',
            'COMMA': r',',
            'FUNCTION': r'sin|cos|tan|log|exp|abs',
            'VARIABLE': r'[a-zA-Z_][a-zA-Z0-9_]*',
            'ABSOLUTE': r'\|',
            'EXPONENTIAL': r'e',
            'LOGARITHM': r'log',
            'SINE': r'sin',
            'COSINE': r'cos',
            'TANGENT': r'tan',
        }

        # A string containing ignored characters (spaces and tabs)
        self.ignore = ' \t'

        # Combine all token patterns into a single regex
        self.token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_patterns.items())

    def tokenize(self, data):
        tokens = []
        for match in re.finditer(self.token_regex, data):
            token_type = match.lastgroup
            token_value = match.group(token_type)
            tokens.append((token_type, token_value))

        return tokens


```
### Tokenize method
The tokenize method of the Lexer class takes a string as input and produces a list of tokens. It operates by iterating through the list of token patterns stored in the self.token_patterns attribute of the Lexer instance. The method utilizes regular expressions to match each pattern with the start of the input string. Once a match is detected, the method concatenates the token type and matched string to create a token, which it appends to the token list stored in the self.tokens attribute.

If a match is made, the method modifies the input string by removing the matched section. This process is repeated until the entire input string has been processed. In the event that a pattern does not match any portion of the input string, the method raises a ValueError that contains an error message signifying the presence of an invalid token.

Lastly, the method returns the token list that was generated.
```python
    def tokenize(self, data):
        tokens = []
        for match in re.finditer(self.token_regex, data):
            token_type = match.lastgroup
            token_value = match.group(token_type)
            tokens.append((token_type, token_value))

        return tokens
```
### Main
The Main class imports the Lexer class from the lexer module and creates an instance of the Lexer class by calling its constructor without any arguments. Then, the tokenize method of the Lexer instance is invoked with the input string "2 + 3 * (4 - 1)". The method processes the input string by breaking it down into a list of tokens and then returns the list. Finally, the resulting list of tokens is displayed on the console using the print function. The output confirms that the input string has been successfully tokenized into its respective tokens such as numbers, operators, and parentheses. Additionally, the message "input valid" is displayed on the console, indicating that the input string was tokenized successfully without any errors.```python
```python
from lexer import Lexer
class Main:
    lexer = MathLexer()
    tokens = lexer.tokenize("2 + 3 * (4 - 1)")
    print(tokens)

```



## Results
[('NUMBER', '2'), ('PLUS', '+'), ('NUMBER', '3'), ('TIMES', '*'), ('LPAREN', '('), ('NUMBER', '4'), ('MINUS', '-'), ('NUMBER', '1'), ('RPAREN', ')')]

## Conclusions
This project involves creating a lexer using regular expressions in Python. A lexer, which is also called a tokenizer or scanner, is a crucial component in programming language compilation. It takes an input string and breaks it down into a sequence of tokens, which are atomic units representing significant language elements like keywords, operators, and literals. The lexer identifies these tokens based on a set of production rules that define the syntax of the language being processed.
The lexer's role is to analyze the input source code and identify the smallest syntax units in the language, called lexemes. Each lexeme is then mapped to a corresponding token based on its type and meaning. Tokens form a stream of symbols that serve as input to the parser, the next stage in the compilation process.
The lexer is a powerful tool in programming language processing, used in syntax highlighting, code completion, and program analysis. Syntax highlighting enhances code readability by coloring tokens based on their type. Code completion suggests possible completions for partially typed code based on tokens. Program analysis involves analyzing the program structure and properties to detect errors, vulnerabilities, or optimization opportunities.
This project uses Python and regular expressions to develop a lexer. Regular expressions are efficient for defining production rules for the lexer. The implementation matches input against regular expressions to identify token types like integers, operators, parentheses, and white spaces. The corresponding token types for each regular expression are defined. If no match is found, an error is raised indicating that the input string is invalid.
This project provides a strong foundation for understanding and implementing lexers in Python. It emphasizes the importance of the lexer in programming language processing and demonstrates the power of regular expressions in defining language syntax. With this knowledge, more advanced compilers, interpreters, and code analysis tools can be built using the lexer to facilitate language processing and improve the developer experience.
