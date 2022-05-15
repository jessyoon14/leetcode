class Logger:
    """
    Queue + set
    time: O(n)
    space: O(n)
    """

    def __init__(self):
        self.recent_messages = set()
        self.message_queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # update queue and set to only contain recent messages
        while self.message_queue and self.message_queue[0][0] < timestamp - 9:
            prev_timestamp, prev_message = self.message_queue.popleft()
            self.recent_messages.remove(prev_message)

        if message not in self.recent_messages:
            self.recent_messages.add(message)
            self.message_queue.append((timestamp, message))
            return True
        else:
            return False

    """
    Dictionary (hashtable)
    Time: O(1)
    Space: O(m) -> m: size of all incoming messages (over time, the hashtable would get super big)
    """

    def __init__(self):
        self.last_printed_at = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.last_printed_at and self.last_printed_at[message] + 10 > timestamp:
            return False
        else:
            self.last_printed_at[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
