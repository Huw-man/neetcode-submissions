class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        plow = float("inf")
        profit = 0
        for i, p in enumerate(prices):
            if p - plow > profit:
                profit = p - plow
            plow = min(p, plow)
        return profit