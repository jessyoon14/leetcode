#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    def __init__(self):
        self.queue = []
        self.stack = []

    def push(self, x: int) -> None:
        # store in stack
        self.stack.append(x)

    def pop(self) -> int:
        # pop from queue. if queue empty, fill queue with stack
        if not self.queue and self.stack:
            while self.stack:
                self.queue.append(self.stack.pop())
        return self.queue.pop()

    def peek(self) -> int:
        # peek from queue. if queue empty, fill queue with stack
        if not self.queue and self.stack:
            while self.stack:
                self.queue.append(self.stack.pop())
        return self.queue[-1]

    def empty(self) -> bool:
        # check queue and stack
        return not self.queue and not self.stack


# class MyQueue:

#     def __init__(self):
#         self.helper = []
#         self.queue = []


#     def push(self, x: int) -> None:
#         # store queue in helper
#         while self.queue:
#             self.helper.append(self.queue.pop())

#         # store input in queue
#         self.queue.append(x)

#         # restore values to queu
#         while self.helper:
#             self.queue.append(self.helper.pop())

#     def pop(self) -> int:
#         return self.queue.pop()

#     def peek(self) -> int:
#         return self.queue[-1]

#     def empty(self) -> bool:
#         return len(self.queue) == 0


# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()


# @lc code=end
