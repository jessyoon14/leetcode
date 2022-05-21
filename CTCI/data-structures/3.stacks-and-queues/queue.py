class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        node = QueueNode(data)
        if self.last:
            self.last.next = node
        else:
            self.first = node
        self.last = node

    def remove(self):
        if self.first is None:
            raise Exception('Cannot remove from empty queue')
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return data

    def peek(self):
        if self.first is None:
            raise Exception('Cannot peek from empty queue')
        return self.first.data

    def is_empty(self):
        return self.first is None


q = Queue()
# print(q.remove())
# print(q.peek())
print(q.add(1))
print(q.remove())
print(q.is_empty())
print(q.add(2))
print(q.add(3))
print(q.add(4))
print(q.remove())
print(q.remove())
print(q.remove())
