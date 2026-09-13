class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i not in ["+", "C", "D"]:
                stack.append(int(i))

            elif i == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a)
                stack.append(b)
                stack.append(a+b)

            elif i == "C":
                stack.pop()

            elif i == "D":
                b = stack.pop()
                stack.append(b)
                stack.append(2*b)
            
        print(stack)
        total = 0
        for i in stack:
            total += i

        return total