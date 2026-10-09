class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                word = ""
                num = ""
                while stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*word)
        return "".join(stack)