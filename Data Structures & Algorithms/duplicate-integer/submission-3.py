class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numd = dict()
        for i in nums:
            numd[i] = 1 + numd.get(i,0)
            if numd[i] > 1 :
                return True
        return False