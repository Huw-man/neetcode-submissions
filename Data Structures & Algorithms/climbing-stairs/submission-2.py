class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs2(self, n: int) -> int:
        cache = [0]*(n+1)
        def climbR(n, cache):
            if cache[n] > 0:
                return cache[n]

            if n < 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            t = climbR(n-1, cache) + climbR(n-2, cache)
            cache[n] = t
            return t
        return climbR(n, cache)
    