class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, tree):
        node_type = tree[0]

        if node_type == 'NUM':
            return float(tree[1])

        if node_type == 'ADD':
            left_value = self.interpret(tree[1])
            right_value = self.interpret(tree[2])
            return left_value + right_value

        if node_type == 'SUB':
            left_value = self.interpret(tree[1])
            right_value = self.interpret(tree[2])
            return left_value - right_value

        if node_type == 'MUL':
            left_value = self.interpret(tree[1])
            right_value = self.interpret(tree[2])
            return left_value * right_value

        if node_type == 'DIV':
            left_value = self.interpret(tree[1])
            right_value = self.interpret(tree[2])
            return left_value / right_value

        raise ValueError(f"Invalid node type: {node_type}")
