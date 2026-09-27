class Solution:

    def operation(self,a,b,i):
        

        match i:
            case "+": 
                return a + b
            case "-": 
                return a - b
            case "*":
                return a * b
            case "/":
                return int(a / b)


    def evalRPN(self, tokens: List[str]) -> int:
        
        result = 0
        stack = []
        for i in tokens:
            if i.lstrip("-").isdigit():
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(str(self.operation(int(a),int(b),i)))

        return int(stack[0])