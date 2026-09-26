class MyStack:

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        count = 0
        element_pop = 0
        while self.q1:
            element_pop = self.q1.popleft()
            self.q2.append(element_pop)
            count+=1

        element = 0
        for i in range(count-1):
            element = self.q2.popleft()
            self.q1.append(element)

        
        return self.q2.popleft()

    def top(self) -> int:
        element = 0
        while self.q1:
            element = self.q1.popleft()
            self.q2.append(element)
        
        while self.q2:
            element = self.q2.popleft()
            self.q1.append(element)

        
        return element

    def empty(self) -> bool:
        if self.q1:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()