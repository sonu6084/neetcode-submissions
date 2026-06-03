class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0,len(nums)):
            k = i+1
            j = len(nums)-1
            while k<j:
                target = nums[i] + nums[k] + nums[j]
                if target < 0:
                    k+=1
                elif target > 0: 
                    j-=1
                else:
                    ans = []
                    ans.append(nums[i])
                    ans.append(nums[k])
                    ans.append(nums[j])
                    ans.sort()
                    if ans not in res:
                        res.append(ans)
                    k+=1
                    j-=1
        return res
                