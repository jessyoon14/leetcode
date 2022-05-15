#
# @lc app=leetcode id=2034 lang=python3
#
# [2034] Stock Price Fluctuation
#

# @lc code=start

import heapq

"""
Dict + Heap
"""


class StockPrice:

    def __init__(self):
        self.prices = {}
        self.min_heap = []
        self.max_heap = []
        self.latest_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.latest_timestamp = max(timestamp, self.latest_timestamp)

        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.latest_timestamp]

    def maximum(self) -> int:
        curr_price, timestamp = heappop(self.max_heap)

        while -curr_price != self.prices[timestamp]:
            curr_price, timestamp = heappop(self.max_heap)
        heapq.heappush(self.max_heap, (curr_price, timestamp))

        return -curr_price

    def minimum(self) -> int:
        curr_price, timestamp = heappop(self.min_heap)
        while curr_price != self.prices[timestamp]:
            curr_price, timestamp = heappop(self.min_heap)
        heapq.heappush(self.min_heap, (curr_price, timestamp))

        return curr_price

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end
