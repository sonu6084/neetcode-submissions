class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran_dict = {"}" : "{", "]" : "[", ")" : "("}

        for i in s:
            if i not in paran_dict:
                stack.append(i)
            else:
                if stack and stack[-1] == paran_dict[i] :
                    stack.pop()
                else:
                    stack.append(i)


        if stack:
            return False
        else: 
            return True