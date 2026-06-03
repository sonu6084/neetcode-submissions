class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        capacity = 0
        while i < j:
            curr = min(heights[j],heights[i]) * (j-i)
            capacity = max(curr,capacity)
            if heights[j] > heights[i]:
                 i+=1
            else:
                j-=1
        return capacity