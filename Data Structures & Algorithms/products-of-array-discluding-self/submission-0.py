class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy() 
        postfix = nums.copy()

        
        for i in range(1,len(nums)):
            prefix[i] *= prefix[i-1]

        for i in range(len(nums)-2,0,-1):
            postfix[i] *= postfix[i+1]

        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i+1]
            elif i == len(nums)-1:
                nums[i] = prefix[i-1]
            else:
                nums[i] = prefix[i-1]*postfix[i+1]

        print(prefix)
        print(postfix)
        return nums