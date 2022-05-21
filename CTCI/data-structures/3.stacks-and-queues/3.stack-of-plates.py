"""
pop() returns None if empty
"""


import unittest


class Stack:
    """push, pop, size"""

    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, item):
        if self.size() >= capacity:
            raise Exception('Cannot push to full stack')
        self.stack.append(item)

    def pop(self):
        if not stack:
            return None
        return self.stack.pop()

    def is_full(self):
        return self.size() >= self.capacity

    def size(self):
        return len(self.stack)


class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, item):
        if not self.stacks or self.stacks[-1].is_full():
            curr_stack = Stack()
            self.stacks.append(curr_stack)
        else:
            curr_stack = self.stacks[-1]
        curr_stack.push(item)

    def pop(self, item):
        while self.stacks:
            curr_stack = self.stack[-1]
            if curr_stack:
                return curr_stack.pop()
            else:
                self.stacks.pop()
        return None


"""
Set of Stacks with pop_at
Official solution: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_03/p03_stack_of_plates.py
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    # push: return True on success, False on fail
    def push(self, v):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(v)
        if self.size == 1:
            self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True

    def pop(self):
        if not self.top:
            return None
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value

    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.size -= 1
        return b.value


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

    def is_empty(self):
        last = self.get_last_stack()
        return not last or last.is_empty()

    def push(self, v):
        last = self.get_last_stack()
        if last and not last.is_full():
            last.push(v)
        else:
            stack = Stack(self.capacity)
            stack.push(v)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        v = last.pop()
        if last.size == 0:
            del self.stacks[-1]
        return v

    def pop_at(self, index):
        return self.left_shift(index, True)

    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if stack.is_empty():
            del self.stacks[index]
        elif len(self.stacks) > index + 1:
            v = self.left_shift(index + 1, False)
            stack.push(v)
        return removed_item
