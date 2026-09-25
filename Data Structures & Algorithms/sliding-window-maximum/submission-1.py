class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        output = []
        q = collections.deque()

        # putting indexes in queue
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # element inserted 
            q.append(r)

            # removing left most
            if l > q[0]:
                q.popleft()

            # output result
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1

            r+=1
        return output