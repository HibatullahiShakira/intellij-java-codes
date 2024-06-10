class MyQueue:

    def __init__(self):
        self.queue = []

    def adding_element_to_queue(self, item):
        self.queue.append(item)

    def pop(self):
        del self.queue[0]
        return self.queue
