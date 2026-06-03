class Solution:

    def binarySearch(self,nums,low,high,target):
        if high < low:
            return -1

        mid = int((low+high)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(nums,low,mid-1,target)
        else:
            return self.binarySearch(nums,mid+1,high,target)

    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1

        return self.binarySearch(nums,low,high,target)
        