class FiniteAutomaton:
    def __init__(self, automaton):
        self.states = automaton['states']

        self.alphabet = automaton['alphabet']

        self.transition = automaton['transitions']

        self.start_state = automaton['start_state']

        self.final_states = automaton['final_states']

    # Checks if the given string is accepted by the finite automaton.
    def check_string(self, string):
        current_state = self.start_state

        for symbol in string:
            try:
                current_state = self.transition[current_state][symbol]
            except KeyError:
                return False

        return current_state in self.final_states

    def check_strings(self, strings):
        # Iterates over each string in the input list.
        for string in strings:
            if self.check_string(string):
                # If the string is accepted, prints a message indicating so.
                print(f'String "{string}" is accepted by the automaton.')
            else:
                # If the string is rejected, prints a message indicating so.
                print(f'String "{string}" is rejected by the automaton.')
