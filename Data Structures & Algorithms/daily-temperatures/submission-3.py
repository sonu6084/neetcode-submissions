class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = [i,temperatures[i]]
            if not stack:
                stack.append(temp)
            else:
                while stack and temperatures[i] > stack[-1][1] :
                    res[stack[-1][0]] = i-stack[-1][0]
                    stack.pop()
                stack.append(temp)

        return res