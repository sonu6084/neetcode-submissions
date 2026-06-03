class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sub = []
        longest = 0
        length = 0
        for i in s:
            if i not in sub:
                sub.append(i)   
            else:
                while i in sub:
                    sub = sub[1:]
                sub.append(i)
            longest = max(longest,len(sub))
            

        return longest
