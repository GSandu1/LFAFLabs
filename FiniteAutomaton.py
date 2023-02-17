class FiniteAutomaton:
    # Initialize the states, alphabet, transitions, start state, and final states from the given automaton
    def __init__(self, automaton):
        self.states = automaton['states']
        self.alphabet = automaton['alphabet']
        self.transitions = automaton['transitions']
        self.start_state = automaton['start_state']
        self.final_states = automaton['final_states']

    def verify_string(self, string):
        current_state = self.start_state
         # For each symbol in the string, follow the corresponding transition if it exists
        for symbol in string:
            try:
                current_state = self.transitions[current_state][symbol]
            except KeyError:
             # If the transition does not exist, the string is not valid
                return False

        return current_state in self.final_states

    def verify_strings(self, strings):
        print(f'------------------------------------------------------------------------')
        for string in strings:
            if self.verify_string(string):
                print(f'String "{string}" is valid.')
                print(f'------------------------------------------------------------------------')
            else:
                print(f'String "{string}" is not valid.')
                print(f'------------------------------------------------------------------------')

