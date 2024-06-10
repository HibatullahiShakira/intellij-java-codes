class MyStack:

    def __init__(self):
        self.shakira = []

    def adding_to_stack(self, item):
        self.shakira.append(item)

    def pop(self):
        del self.shakira[-1]
        return self.shakira
