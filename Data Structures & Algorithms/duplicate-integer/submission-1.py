class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupdict = {}
        for i in nums:
            dupdict[i] = 1 + dupdict.get(i,0)
            if dupdict[i] > 1:
                return True

        return False