class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if max_profit < prices[i] - buy:
                max_profit = prices[i] - buy
            if buy > prices[i]:
                buy = prices[i]

        return max_profit