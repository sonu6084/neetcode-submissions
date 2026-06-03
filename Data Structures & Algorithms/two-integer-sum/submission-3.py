class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        res = []
        for i in range(len(nums)):
            if ((target-nums[i]) in check):
                res.append(check[target-nums[i]])
                res.append(i)
                return res
            else:
                check[nums[i]] = i
        return res