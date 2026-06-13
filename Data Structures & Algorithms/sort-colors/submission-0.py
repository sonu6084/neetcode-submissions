class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## three pointers approach 

        L,R,i = 0,len(nums)-1,0

        while i<=R:
            if nums[i]==0:
                nums[i],nums[L] = nums[L],nums[i]
                L+=1
            elif nums[i]==2:
                nums[i],nums[R] = nums[R],nums[i]
                R-=1
                i-=1
            i+=1
        