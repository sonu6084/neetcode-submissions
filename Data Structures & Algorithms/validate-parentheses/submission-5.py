class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        if len(s) == 1:
            return False

        for i in s:
            if i not in paran.keys():
                stack.append(i)
            elif not stack or stack[-1] != paran[i]:
                stack.append(i)
            else:
                stack.pop()
        if not stack:
            return True
        else:
            return False