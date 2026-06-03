class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasht = {}
        hashs = {}

        for i in range(len(t)):
            hasht[t[i]] = 1 + hasht.get(t[i],0)

        for i in range(len(s)):
            hashs[s[i]] = 1 + hashs.get(s[i],0)

        return hasht == hashs