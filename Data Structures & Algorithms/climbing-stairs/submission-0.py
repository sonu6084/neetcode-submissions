class Solution:

    def fib(self,n,fiboarr):
        if(n<=1):
            return fiboarr[n]
        if(fiboarr[n] != -1):
            return fiboarr[n]
        fiboarr[n] = self.fib(n-1,fiboarr) + self.fib(n-2,fiboarr)
        return fiboarr[n]

    def climbStairs(self, n: int) -> int:
        fiboarr = [-1]*(n+1)
        fiboarr[0] = 1
        fiboarr[1] = 1
        self.fib(n,fiboarr)
        print(fiboarr)

        return fiboarr[-1]