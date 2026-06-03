class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = []
        for i in strs:
            strs_sorted.append("".join(sorted(i)))
        anagrams = {}
        
        print(strs_sorted)
        for i in range(0,len(strs_sorted)):
            anagrams[strs_sorted[i]] = []

        for i in range(0,len(strs_sorted)):
            anagrams[strs_sorted[i]].append(strs[i])


        res = []
        for i in anagrams.values():
            res.append(i)
        return res 
