class Solution:

    def rob2(self,nums):
        robs = []
        robs.append(0)
        robs.append(0)
        robs = robs + nums


        for i in range(2,len(robs)):
            robs[i] = max(robs[i-1],robs[i]+robs[i-2])

        
        print(robs)
        return robs[-1]

    def rob(self, nums: List[int]) -> int:


        n = len(nums)

        if n < 2:
            return nums[0]
        return max(self.rob2(nums[:n-1]),self.rob2(nums[1:]))
        

        