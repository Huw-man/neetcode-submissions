class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        base = coins[:]   


    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def coin_traverse(amount):
            if amount < 0:
                return -1
            elif amount == 0:
                return 0
            elif amount in memo:
                return memo[amount]

            
            ncoins = float('inf')
            for c in coins:
                tc = coin_traverse(amount - c)
                if tc > -1:
                    ncoins = min(ncoins, tc + 1)
    
            if ncoins == float('inf'):
                ncoins = -1
            else:
                ncoins = ncoins
            memo[amount] = ncoins
            return ncoins
        
        return coin_traverse(amount)