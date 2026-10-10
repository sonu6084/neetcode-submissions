from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(list)
        self.maxf = 1

    def push(self, val: int) -> None:

        curr = 1

        while curr <= self.maxf:
            if curr not in self.freq:
                self.freq[curr].append(val)

                break

            if val not in self.freq[curr]:
                self.freq[curr].append(val)
                break
            else:
                curr+=1

            self.maxf = max(curr,self.maxf)
        # print(self.freq)

    def pop(self) -> int:
        
        
        if self.freq[self.maxf]:
            pass
        else:
            self.maxf-=1
        return self.freq[self.maxf].pop()
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()