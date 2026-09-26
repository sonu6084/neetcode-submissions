class MinStack:

    def __init__(self):
        self.s1 = []
        self.mins = float('inf')
        self.ms = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if self.mins > val or len(self.s1) == 1:
            self.mins = val
            self.ms.append(val)
        

    def pop(self) -> None:
        element = self.s1.pop()
        if self.ms[-1] == element and element not in self.s1:
            self.ms.pop()


    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.ms[-1]
