class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs.sort()
        print(strs)
        for i in range(0,len(strs[0])):
            for s in strs:
                if s[i] != strs[0][i]:
                    return prefix
                
            prefix+=s[i]
        return prefix
