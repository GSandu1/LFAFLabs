import matplotlib.pyplot as plt
import networkx as nx
from Automaton import Automaton
from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammars
from lexer import MathLexer
class Main:
    # Initialize the Main class by setting up a grammar,
    def __init__(self):
        self.productions = {
            'S': ['aA', 'aB'],
            'A': ['bS'],
            'B': ['aC'],
            'C': ['a', 'bS'],
        }
        self.start_symbol = 'S'
        self.grammar = Grammars(self.productions, self.start_symbol)
        self.finite_automaton = self.grammar.to_finite_automaton()
        self.automaton = FiniteAutomaton

    # Generates strings from the grammar
    def generate_strings(self, num_strings):
        for i in range(num_strings):
            string = self.grammar.generate_string()
            print(string)

if __name__ == '__main__':
    main = Main()

    main.generate_strings(5)

    automatons = main.grammar.to_finite_automaton()

    # Define a finite automaton manually
    automaton = {
        'states': {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
        'alphabet': {'a', 'b', 'c'},
        'transitions': {
        'q0': {'a': 'q1'},
        'q1': {'a': 'q4', 'b': 'q2', 'c': 'q5'},
        'q2': {'a': 'q3', 'b': 'q2', 'c': 'q5'},
        'q3': {'a': 'q3', 'b': 'q4', 'c': 'q5'},
        'q4': {'a': 'q3', 'b': 'q2', 'c': 'q5'},
        'q5': {'a': 'q5', 'b': 'q0', 'c': 'q5'}
    },
        'start_state': 'q0',
        'final_states': {'q3', 'q5'}
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
                   ('q1', 'a'): ['q1','q2'],
                   ('q1', 'b'): ['q3'],
                   ('q2', 'a'): ['q2'],
                   ('q2', 'b'): ['q3']}

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

# Convert NDFA to DFA
dfa = automation.to_dfa()
print(f"DFA states: {dfa.states}")
print(f"DFA transition function: {dfa.transitions}")
print(f"DFA initial state: {dfa.start_state}")
print(f"DFA final states: {dfa.accept_states}")

# Convert automaton to regular grammar
grammar = automation.to_grammar()
print(f"Regular grammar productions: {grammar}")
print(main.grammar.chomsky_classification())
automation.render()

print('-------------------------------------------------------------------LAB3-------------------------------------------------------------------------')

lexer = MathLexer()
tokens = lexer.tokenize("2 + 3 * (4 - 1)")
print(tokens)

