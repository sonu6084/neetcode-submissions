import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        largest = 0
        for i in range(k):
            largest = heapq._heappop_max(nums)

        return largest

        import random
