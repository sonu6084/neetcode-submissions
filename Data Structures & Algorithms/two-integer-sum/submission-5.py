class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        res = []
        for i,n in enumerate(nums):
            if ((target-n) in check):
                res.append(check[target-n])
                res.append(i)
                return res
            else:
                check[n] = i
        return res