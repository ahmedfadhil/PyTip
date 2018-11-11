
"""Stack data structure"""


class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        pass

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def get_stack(self):
        return self.items
