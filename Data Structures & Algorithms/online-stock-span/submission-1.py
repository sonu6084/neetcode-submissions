class StockSpanner:

    def __init__(self):
        self.stack = []
        self.sstack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            return 1
        
        count = 1
        while self.stack and price >= self.stack[-1]:
            count+=1
            self.sstack.append(self.stack.pop())

        while self.sstack:
            self.stack.append(self.sstack.pop())

        self.stack.append(price)
        return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)