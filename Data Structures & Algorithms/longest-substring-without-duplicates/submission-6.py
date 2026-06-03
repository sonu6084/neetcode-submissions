class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = [-1 for _ in range(256)]
        print(ord('a'))
        l = 0
        r = 0
        longest = 0
        for r in range(len(s)):
            if hashmap[ord(s[r])] != -1:
                if hashmap[ord(s[r])] >=l:
                    l = hashmap[ord(s[r])] + 1
                
            
            hashmap[ord(s[r])] = r
            longest = max(longest,r-l+1)
        return longest