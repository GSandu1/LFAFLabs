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
