class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            k = i+1
            j = len(nums)-1
            while k<j:
                target = nums[i] + nums[k] + nums[j]
                if target < 0:
                    k+=1
                elif target > 0: 
                    j-=1
                else:
                    res.append([nums[i], nums[k], nums[j]])
                    k+= 1
                    j-= 1
                    while k < j and nums[k] == nums[k-1]:
                        k+= 1
                    while k < j and nums[j] == nums[j+1]:
                        j-= 1
                    
        return res
                