from Automaton.Automaton import Automaton
from Automaton.FiniteAutomaton import FiniteAutomaton
from Grammar.Grammar import Grammars
from Chomsky.ChomskyConverter import CNFConverter
from Grammar.lexer import Lexer as MathLexer
from Parser.parser import Parser
from Parser.interpreter import Interpreter


class Main:
    def __init__(self):
        self.productions = {
            'S': ['aA'],
            'A': ['aA', 'b']
        }
        self.start_symbol = 'S'
        self.grammar = Grammars(self.productions, self.start_symbol)
        self.finite_automaton = self.grammar.to_finite_automaton()
        self.automaton = FiniteAutomaton

    def generate_strings(self, num_strings):
        for i in range(num_strings):
            string = self.grammar.generate_string()
            print(string)

    def process_expression(self, expression):
        lexer = MathLexer()
        tokens = lexer.tokenize(expression)
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        result = interpreter.interpret(ast)
        print(f"Result of {expression} is {result}")


def main():
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('                                                                                     LAB1')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    main_obj = Main()

    main_obj.generate_strings(5)

    automatons = main_obj.grammar.to_finite_automaton()

    automaton = {
        'states': {'q0', 'q1', 'q2', 'q3'},
        'alphabet': {'a', 'b'},
        'transitions': {
            'q0': {'a': 'q0', 'b': 'q1'},
            'q1': {'a': 'q2', 'b': 'q1'},
            'q2': {'a': 'q2', 'b': 'q3'},
            'q3': {'a': 'q2', 'b': 'q3'}
        },
        'start_state': 'q0',
        'final_states': {'q3'}
    }

    checker = FiniteAutomaton(automaton)

    checker.check_strings(['aaa', 'abaaa', 'ababaa', 'aa', 'abababa'])

    print(automatons)

    automation = Automaton()

    automation.states = ['q0', 'q1', 'q2', 'q3']
    automation.alphabet = ['a', 'b']
    automation.transitions = {
        ('q0', 'a'): ['q0'],
        ('q0', 'b'): ['q1'],
        ('q1', 'a'): ['q1', 'q2'],
        ('q1', 'b'): ['q3'],
        ('q2', 'a'): ['q2'],
        ('q2', 'b'): ['q3']
    }

    automation.start_state = 'q0'
    automation.accept_states = ['q3']

    print('')
    print('')
    print('')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('                                                                                     LAB2')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    is_deterministic = automation.is_deterministic()
    print(f"Is automaton deterministic? {is_deterministic}")

    dfa = automation.to_dfa()
    print(f"DFA states: {dfa.states}")
    print(f"DFA transition function: {dfa.transitions}")
    print(f"DFA initial state: {dfa.start_state}")
    print(f"DFA final states: {dfa.accept_states}")

    grammar = automation.to_grammar()
    print(f"Regular grammar productions: {grammar}")
    print(main_obj.grammar.chomsky_classification())

    print('')
    print('')
    print('')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('                                                                                     LAB3')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    lexer = MathLexer()
    tokens = lexer.tokenize("2 + 3 * (4 - 1)")
    print(tokens)

    print('')
    print('')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('                                                                                     LAB4')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    VN = {'S', 'A', 'B', 'C', 'D'}
    VI = {'a', 'b'}
    P = [
        ('S', ('a', 'B')),
        ('S', ('D', 'A')),
        ('A', ('a',)),
        ('A', ('B', 'D')),
        ('A', ('b', 'D', 'A', 'B')),
        ('B', ('b',)),
        ('B', ('B', 'A')),
        ('D', ()),
        ('D', ('B', 'A')),
        ('C', ('B', 'A')),
    ]
    S = 'S'
    grammar = (VN, VI, P, S)

    cnf_converter = CNFConverter(grammar)
    cnf_grammar = cnf_converter.convert_to_cnf()

    print('Original grammar:')
    print(grammar)
    print('Grammar in Chomsky normal form:')
    print(cnf_grammar)

    print('')
    print('')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('                                                                                     LAB5')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    main_obj.process_expression("2 + 3 * (4 - 1)")


if __name__ == '__main__':
    main()
