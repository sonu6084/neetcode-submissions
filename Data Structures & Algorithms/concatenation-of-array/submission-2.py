class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = 2*n*[0]
        for i in range(0,len(nums)):
            ans[i]=nums[i]
            ans[n+i]=nums[i]
        return ans