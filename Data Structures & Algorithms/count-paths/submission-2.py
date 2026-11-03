class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(m, n):
            if m == 0 and n == 0:
                return 1
            if m < 0 or n < 0:
                return 0
            if (m, n) in memo:
                return memo[(m, n)]

            res = dfs(m - 1, n) + dfs(m, n - 1)
            memo[(m, n)] = res
            return res

        return dfs(m-1, n-1)