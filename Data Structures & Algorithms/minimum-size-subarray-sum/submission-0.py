class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = 0
        l = 0
        summ = 0
        res = float('inf')
        while r < len(nums):
            summ += nums[r]
            while summ >= target:
                res = min(res,r-l+1)
                summ -= nums[l]
                l+=1 
            r+=1
                    
        return res if res!=float('inf') else 0