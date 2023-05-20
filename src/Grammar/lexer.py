# import re
#
# class MathLexer:
#     def __init__(self):
#         self.token_patterns = {
#             'NUMBER': r'\d+',
#             'PLUS': r'\+',
#             'MINUS': r'-',
#             'TIMES': r'\*',
#             'DIVIDE': r'/',
#             'LPAREN': r'\(',
#             'RPAREN': r'\)',
#             'POWER': r'\^',
#             'MODULO': r'%',
#             'EQUALS': r'=',
#             'COMMA': r',',
#             'FUNCTION': r'sin|cos|tan|log|exp|abs',
#             'VARIABLE': r'[a-zA-Z_][a-zA-Z0-9_]*',
#             'ABSOLUTE': r'\|',
#             'EXPONENTIAL': r'e',
#             'LOGARITHM': r'log',
#             'SINE': r'sin',
#             'COSINE': r'cos',
#             'TANGENT': r'tan',
#         }
#
#         # A string containing ignored characters (spaces and tabs)
#         self.ignore = ' \t'
#
#         # Combine all token patterns into a single regex
#         self.token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_patterns.items())
#
#     def tokenize(self, data):
#         tokens = []
#         for match in re.finditer(self.token_regex, data):
#             token_type = match.lastgroup
#             token_value = match.group(token_type)
#             tokens.append((token_type, token_value))
#
#         return tokens

import re

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self):
        self.token_types = {
            'NUMBER': r'\d+(\.\d+)?',
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
            'SPACE': r'\s+'  # Matches one or more space characters
        }

    def tokenize(self, source_code):
        tokens = []
        while source_code != '':
            for token_type, pattern in self.token_types.items():
                match = re.match(pattern, source_code)
                if match:
                    value = match.group(0)
                    if token_type != 'SPACE':  # skip spaces
                        tokens.append(Token(token_type, value))
                    source_code = source_code[len(value):]
                    break
            else:
                raise Exception(f"Unexpected character: '{source_code[0]}'")
        return tokens
