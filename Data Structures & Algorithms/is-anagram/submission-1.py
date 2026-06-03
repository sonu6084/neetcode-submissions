class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}
        if len(s)==len(t):
            for i in s:
                if i in hashs.keys():
                    hashs[i]+=1
                else:
                    hashs[i]=1
            for i in t:
                if i in hasht.keys():
                    hasht[i]+=1
                else:
                    hasht[i]=1

            return hasht == hashs
            # for i in hashs.keys():
            #     try:
            #         if hashs[i] != hasht[i]:
            #             return False
            #     except KeyError as e:
            #         return False
            # return True
        else:
            return False