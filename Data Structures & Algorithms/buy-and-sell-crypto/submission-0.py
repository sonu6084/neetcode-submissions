class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # make window from 2 to len - 1
        window = 2
        maxi = 0
        for i in range(len(prices)):
            window = 1
            while i + window < len(prices):
                maxi = max(maxi,prices[i+window]-prices[i])
                window+=1

        return maxi