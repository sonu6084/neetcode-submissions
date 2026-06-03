class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupdict = {}
        for i in nums:
            if i in dupdict:
                return True
            else:
                dupdict[i]=1
        return False