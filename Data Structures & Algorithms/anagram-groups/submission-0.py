class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for s in strs:
            anagram_dict = {}
            for j in range(0,len(s)):
                anagram_dict[s[j]] = 1 + anagram_dict.get(s[j],0)

            res.append(anagram_dict)
        ans = []

        for dic in range(0,len(strs)):
            ans2 = []
            if res[dic] != -1:
                ans2.append(strs[dic])
                print(ans)
                for j in range(dic+1,len(strs)):
                    if res[dic] == res[j]:
                        ans2.append(strs[j])
                        res[j]=-1
                ans.append(ans2)
            print(res)
            
        return ans