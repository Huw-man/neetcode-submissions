from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            elif s[i] == '0':
                return 0
            elif i in memo:
                return memo[i]

            dec_count = dfs(i+1)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                dec_count += dfs(i+2)

            memo[i] = dec_count
            return dec_count
        
        return dfs(0)

        