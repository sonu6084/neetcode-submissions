class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count  = {}
        l = 0
        res = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
            if (i-l+1)-max(count.values()) <= k:
                res = max(res,i-l+1)
            else:
                count[s[l]] -=1
                l+=1
        return res