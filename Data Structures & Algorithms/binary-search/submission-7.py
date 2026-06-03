class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
        while low<=high:
            mid = int((high+low)/2)
            print(low,high)
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

            if high < low :
                return -1
        return -1