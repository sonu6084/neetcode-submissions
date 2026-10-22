class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x-1
        res = 0
        
        # if x == 0:
        #     return 0
        # if x < 4:
        #     return 1
        
        
        while l <= r:
            mid = (l+r)//2
            if (mid+1)**2 <= x:
                res = mid+1
                l = mid + 1
            else:
                r = mid - 1
        return res