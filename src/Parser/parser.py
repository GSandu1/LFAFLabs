class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next() # Set the first token as the current token

    def next(self):
        self.current_token = self.tokens.pop(0) if self.tokens else None # Get the next token from the input list

    def parse(self):
        print('Parsing expression...')
        return self.expression()

    def expression(self):
        print('Parsing expression: term')
        expr = self.term() # Parse the term
        while self.current_token and self.current_token.type in ('PLUS', 'MINUS'):
            if self.current_token.type == 'PLUS':
                print('Parsing expression: add')
                self.next() # Move to the next token
                expr = ('ADD', expr, self.term())  # Create a node representing addition
            elif self.current_token.type == 'MINUS':
                print('Parsing expression: subtract')
                self.next()  # Move to the next token
                expr = ('SUB', expr, self.term()) # Create a node representing subtraction
        return expr

    def term(self):
        print('Parsing term: factor')
        term = self.factor()
        while self.current_token and self.current_token.type in ('TIMES', 'DIVIDE'):
            if self.current_token.type == 'TIMES': # Create a node representing multiplication
                print('Parsing term: multiply')
                self.next()
                term = ('MUL', term, self.factor())
            elif self.current_token.type == 'DIVIDE':
                print('Parsing term: divide')
                self.next()
                term = ('DIV', term, self.factor())
        return term

    def factor(self):
        if self.current_token.type == 'NUMBER':
            value = self.current_token.value
            print('Parsing factor: number {}'.format(value))
            self.next()
            return ('NUM', value) # Create a node representing a numeric value
        elif self.current_token.type == 'LPAREN':
            print('Parsing factor: expression')
            self.next()
            value = self.expression() # Parse the enclosed expression
            if self.current_token.type != 'RPAREN':
                raise Exception('Expected )')
            self.next()
            return value
        raise Exception('Unexpected token')
