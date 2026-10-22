class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        plow = float("inf")
        profit = 0
        for p in prices:
            profit = max(p - plow, profit)
            plow = min(p, plow)
        return profit