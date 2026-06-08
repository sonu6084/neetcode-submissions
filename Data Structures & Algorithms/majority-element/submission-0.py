class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majdict = {}
        for i in nums:
            majdict[i] = 1 + majdict.get(i,0)

        majel = 0
        freq = 0
        for i in majdict:
            if majdict[i] > freq:
                majel = i
                freq = majdict[i]

        return majel