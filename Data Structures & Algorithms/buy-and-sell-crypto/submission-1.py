class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minvalue = prices[0]
        for i in prices:
            profit = max(profit,i-minvalue)
            minvalue = min(i,minvalue)

        return profit