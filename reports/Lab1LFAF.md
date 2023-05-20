# Topic: Intro to formal languages. Regular grammars. Finite Automata.
## Course: Formal Languages & Finite Automata
## Author: Nistor Stefan FAF-211
Variant 13:

VN={S, B, D}, 

VT={a, b, c}, 

P={ 
    S → aB
    B → aD
    B → bB
    D → aD
    D → bS
    B → cS
    D → c
}

## Theory
Regular Grammars and Finite Automata are fundamental concepts in theoretical computer science
and play a crucial role in the study of formal languages and automata theory.
A Regular Grammar is a set of production rules used to generate strings in a formal language. A
formal language is a set of strings made up of symbols from a given alphabet, and regular grammars describe
a subset of those languages that can be recognized by Finite Automata. Regular grammars are defined by a
set of production rules, which specify how to rewrite a symbol in the language to a string of other symbols.
The production rules are applied repeatedly to generate all the valid strings in the language.
A Finite Automaton is a mathematical model used to recognize patterns in strings, and it consists of a
set of states, an initial state, a set of accepting states, and a transition function that maps from a current state
and input symbol to a next state. Finite automata are classified as either deterministic or non-deterministic,
depending on whether or not multiple transitions are possible for a given input symbol and state.
The relationship between regular grammars and finite automata is very close, and they are often
used interchangeably. In particular, every regular grammar can be associated with a deterministic finite
automaton, and every deterministic finite automaton can be associated with a regular grammar.
Regular grammars and finite automata have numerous applications in computer science, including parsing, pattern matching, lexical analysis, and text processing. They provide a foundation for more
advanced topics, such as context-free grammars, pushdown automata, and Turing machines, which are
essential in the study of computational complexity and algorithm design.
## Objectives:
- Understand what a language is and what it needs to have in order to be considered a formal one.

-  Provide the initial setup for the evolving project that you will work on during this semester. I said
project because usually at lab works, I encourage/impose students to treat all the labs like stages of
development of a whole project. Basically you need to do the following:


    a. Create a local && remote repository of a VCS hosting service

    b. Choose a programming language

    c. Create a separate folder the report will be kept

- According to my variant 6, get the grammar definition and do the following tasks:

    a. Implement a type/class for the grammar;

    b. Add one function that would generate 5 valid strings from the language expressed by the given grammar

    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;

    d. For the Finite Automaton, add a method that checks if an input string can be obtained via the state transition from it
## Implementation description
### Generate String
This code generates a string by applying grammar rules. It has two functions: generate_string and `_generate_string`.
The `generate_string` function simply calls _generate_string with the starting symbol and returns the result.
The `_generate_string` function takes a symbol as input. If the symbol is a terminal, it is returned as is. Otherwise, a random production is chosen for the symbol, and each symbol in the production is recursively processed using _generate_string. The resulting strings are joined together and returned as the final output.
```python
    def generate_string(self):
        return self._generate_string(self.start_symbol)

    def _generate_string(self, symbol):
        if symbol not in self.productions:
            return symbol
        production = random.choice(self.productions[symbol])
        return ''.join(self._generate_string(s) for s in production)

```
### To Finite Automaton
This function converts a grammar into a finite automaton representation.It starts by initializing the starting state as 0 and creating an empty dictionary called `automatons` with the starting state as the key. It also initializes a variable `state_count` to keep track of the number of states.The function then iterates over each symbol in the grammar productions. For each symbol, it iterates over the associated productions.

Inside the inner loop, the function traverses each symbol `s` in the production. It checks if the current state has a transition for symbol s in the `automatons` dictionary. If not, it adds a new state and updates the transition for the current state with the new state. It also adds an empty dictionary for the new state in the `automatons` dictionary. The `state_count` is incremented to keep track of the number of states.

The current state is updated to the newly transitioned state. This process continues until all symbols in the production are processed.After processing all symbols in a production, the function checks if the current state is already present in the `automatons` dictionary. If not, it adds an empty dictionary for the current state.

Finally, the function adds a transition from the current state back to the starting state with an empty string symbol (''). This allows the automaton to loop back to the starting state when it encounters the end of a production.

Once all symbols and productions have been processed, the `automatons` dictionary representing the finite automaton is returned as the output.

```python
    def to_finite_automaton(self):
        start_state = 0
        automatons = {start_state: {}}
        state_count = 1

        for symbol in self.productions:
            for production in self.productions[symbol]:
                current_state = start_state
                for s in production:
                    if s not in automatons[current_state]:
                        automatons[current_state][s] = state_count
                        automatons[state_count] = {}
                        state_count += 1
                    current_state = automatons[current_state][s]
                if current_state not in automatons:
                    automatons[current_state] = {}
                automatons[current_state][''] = start_state

        return automatons
```

### Check String

Here we have two functions related to checking strings against a finite automaton.

The first function, `check_string`, takes a string as input and checks if it is accepted by the automaton. It starts by setting the `current_state` to the starting state of the automaton.

Then, it iterates over each symbol in the input string. For each symbol, it attempts to retrieve the next state from the transition table using the     `current_state` and the symbol as indices. If a KeyError occurs, it means that there is no valid transition for the current state and symbol, so the function immediately returns `False` indicating that the string is not accepted.

If all symbols in the string are successfully processed without encountering any KeyError, the `current_state` is updated to the final state reached after processing the entire string.

Finally, the function checks if the `current_state` is among the final states defined for the automaton. If it is, the function returns `True`, indicating that the string is accepted. Otherwise, it returns `False`.

The second function, `check_strings`, takes a list of strings as input. It iterates over each string in the list and calls the `check_string` function to determine whether each string is accepted or rejected by the automaton. Based on the result, it prints a corresponding message indicating whether each string is accepted or rejected.

```python
def check_string(self, string):
        current_state = self.start_state

        for symbol in string:
            try:
                current_state = self.transition[current_state][symbol]
            except KeyError:
                return False

        return current_state in self.final_states

    def check_strings(self, strings):
        for string in strings:
            if self.check_string(string):
                print(f'String "{string}" is accepted by the automaton.')
            else:
                print(f'String "{string}" is rejected by the automaton.')

```



## Results
aA
aA
aA
aA
aA
String "aaa" is accepted by the automaton.
String "abaaa" is accepted by the automaton.
String "ababaa" is accepted by the automaton.
String "aa" is rejected by the automaton.
String "abababa" is accepted by the automaton.
{0: {'a': 1, 'b': 4, 'c': 6}, 1: {'A': 2, 'D': 3}, 2: {'': 0}, 3: {'': 0}, 4: {'S': 5}, 5: {'': 0}, 6: {'': 0}}

## Conclusions
To comprehend the abilities and constraints of computers, the study of regular grammars and finite automata is crucial. This understanding allows computer scientists to create efficient algorithms for tasks such as text processing, lexical analysis, and pattern matching, which are used in real-world applications like spam filters, data compression, and search engines. Regular grammars and finite automata are essential for computer systems to interact in a standardized manner, which is critical for network communication.
Moreover, studying regular grammars and finite automata has theoretical implications in computer science.Knowing the limitations of these models helps develop more powerful models like context-free grammars,pushdown automata, and Turing machines that can solve more complex problems. Regular grammars and finite automata have connections to other areas of mathematics, such as topology, group theory, and algebra, which provide insight into the relationship between computation and mathematical concepts.
To summarize, regular grammars and finite automata are fundamental concepts in computer science,having practical applications in natural language processing, compilers, and artificial intelligence. They are vital tools to understand computer capabilities and have links to other mathematical fields. With their continued study, regular grammars and finite automata will undoubtedly have a critical role in shaping the future of computer science. 