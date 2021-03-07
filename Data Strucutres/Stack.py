class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self, item):
        self.item.insert(0, item)

    def pop(self):
        return self.item.pop(0)

    def print_stack(self):
        print(self.item)


s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.print_stack()
