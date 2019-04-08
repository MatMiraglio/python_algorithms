class Queue():
    def __init__(self):
        self.array = []

    def enqueue(self, node):
        self.array.append(node)

    def dequeue(self):
        if not len(self.array):
            return None
        item = self.array[0]
        del self.array[0]
        return item

    def is_empty(self):
        if self.array:
            return False

        return True
