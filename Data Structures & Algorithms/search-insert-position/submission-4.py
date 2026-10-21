class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        pos = 0
        # if target <= nums[l]:
        #     return 0
        # if target >= nums[r]:
        #     return len(nums)-1

        while l<=r:
            m = (l + r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
            
        return l