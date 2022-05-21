"""
Reference: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_03/p02_stack_min.py
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, item):
        self.stack.append(item)
        if (self.minimum() is None) or (item <= self.minimum()):
            self.minstack.append(item)

    def pop(self):
        if not self.stack:
            return None
        item = self.stack.pop()
        if self.minimum() and item == self.minimum():
            self.minstack.pop()
        return item

    def minimum(self):
        if self.minstack:
            return self.minstack[-1]
        return None


def test_min_stack():
    newstack = MinStack()
    assert newstack.minimum() is None

    newstack.push(5)
    assert newstack.minimum() == 5

    newstack.push(6)
    assert newstack.minimum() == 5

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.push(7)
    assert newstack.minimum() == 3

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 5

    newstack.push(1)
    assert newstack.minimum() == 1

    print("Pass all tests")


if __name__ == "__main__":
    test_min_stack()
