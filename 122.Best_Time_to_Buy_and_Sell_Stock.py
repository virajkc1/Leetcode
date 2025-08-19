class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        res = 0
        start = n - 1

        while start >= 0:
            i = start
            while i > 0 and prices[i - 1] <= prices[i]:
                i -= 1
            res += prices[start] - prices[i]
            start = i - 1
        
        return res