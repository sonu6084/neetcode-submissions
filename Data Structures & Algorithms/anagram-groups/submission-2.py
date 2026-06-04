class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_ana = []
        for i in strs:
            sorted_ana.append("".join(sorted(i)))
        print(sorted_ana)

        dict_ana = {}
        for i in sorted_ana:
            dict_ana[i] = []

        for i in range(len(sorted_ana)):
            dict_ana[sorted_ana[i]].append(strs[i])

        res = []

        for i in dict_ana:
            res.append(dict_ana[i])

        return res