class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(0,len(nums)):
            
            for k in range(i+1,len(nums)):
                for j in range(k+1,len(nums)):
                    
                    if nums[i] + nums[k] + nums[j] == 0:
                        ans = []
                        ans.append(nums[i])
                        ans.append(nums[k])
                        ans.append(nums[j])
                        ans.sort()
                        if ans not in res:
                            res.append(ans)
        return res
