# Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Gazea Sandu FAF-211





## Theory
    The term "lexer" might sound like a foreign word to you, but it's actually quite important when it comes to programming languages. Essentially, the lexer is responsible for breaking down a string of code into individual "lexemes," which are essentially the smallest units of meaning in a programming language. Think of it like dissecting a sentence into individual words.The lexer is also sometimes called a tokenizer or a scanner, depending on who you ask. But no matter what you call it, the lexer is an essential component of a compiler or interpreter. It's one of the first things that happens when you run a program, and it helps the computer understand what the code is trying to do.

So, how does the lexer work? Well, it uses a set of rules to identify tokens within the code. These tokens can be anything from keywords (like "if" or "else") to symbols (like "+", "-", "*", and "/") to identifiers (like variable names or function names). The lexer then spits out a stream of tokens that the rest of the compiler or interpreter can use to understand what the code is doing.

Overall, the lexer is a crucial component of any programming language, and it's one of the first things you'll learn about when studying computer science. Understanding how the lexer works can help you become a better programmer and give you a deeper appreciation for the way that computers understand and execute code.

## Objectives:
- Understand what lexical analysis is.

- Get familiar with the inner workings of a lexer/scanner/tokenizer.

- Implement a sample lexer and show how it works.
  

## Implementation description
### Lexer class
the Lexer class has the task of examining an input string and detecting the different types of tokens contained within it. It achieves this by establishing a group of patterns that define the various token types, including operators, keywords, identifiers, numbers, and strings, among others. When the tokenize method of the class is invoked, it processes the input string by going through these patterns one by one, trying to find matches. If a match is detected, the token and its value are added to a list of tokens.
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
Have you ever wondered how computers understand programming languages? Well, one important tool they use is called a Lexer. The Lexer takes in a string of code and breaks it down into smaller pieces called tokens, which the computer can then use to understand the code.

The Lexer does this by using something called regular expressions to match patterns in the code. These patterns are stored in a list inside the Lexer, and the Lexer checks each pattern to see if it matches the beginning of the code. If a match is found, the Lexer creates a token by combining the matched pattern with a token type (like a keyword or a variable name), and adds it to a list of tokens.

As the Lexer processes the code, it removes the parts that it has already matched, so that it doesn't repeat any tokens. If the Lexer encounters a pattern that doesn't match any part of the code, it will raise an error to let you know that there's an invalid token in the code.

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
In a program, there's a class called `"Main"` that uses the Lexer to break down code. When the program starts running, it imports the Lexer from a different part of the program and creates a "Lexer instance" which is like a special copy of the Lexer that it can use.Next, the program gives the Lexer instance a string of code to break down. In this case, the code is "2 + 3 * (4 - 1)". The Lexer instance gets to work breaking the code down into individual tokens, like "2", "+", "3", "*", "(", "4", "-", "1", and ")".Once the Lexer instance has finished breaking down the code, it sends the list of tokens back to the program. The program then uses the "print" function to display the list of tokens on the screen.If everything has gone well, the program will display the list of tokens and a message that says "input valid". This means that the Lexer instance was able to break the code down into tokens without any errors.```python
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
In this project, I created a tool called a lexer or tokenizer using Python's regular expressions. This lexer plays a critical role in compiling programming languages by breaking down an input string into smaller syntax units called lexemes, and then mapping each lexeme to a corresponding token. These tokens are the atomic units representing language elements and they form a stream of symbols that are used as input to the parser in the next stage of the compilation process.

Using Python and regular expressions, I builded a lexer that identifies different types of tokens like integers, operators, parentheses, and white spaces, and matches them with corresponding regular expressions. If the lexer doesn't find a match, it raises an error indicating that the input string is invalid.

Overall, this project demonstrates the importance of the lexer in programming language processing and the power of regular expressions in defining language syntax. With this knowledge, I can build more advanced compilers, interpreters, and code analysis tools, ultimately improving the developer experience.