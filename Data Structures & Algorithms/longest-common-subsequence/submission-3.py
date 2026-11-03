class Solution:
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     pass

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i1, i2) -> int:
            if i1 >= len(text1) or i2 >= len(text2) :
                return 0
            if (i1, i2) in memo:
                return memo[i1, i2]

            max_len = max(dfs(i1+1, i2), dfs(i1, i2+1))

            if text1[i1] == text2[i2]:
                max_len = max(max_len, 1 + dfs(i1+1, i2+1))
            
            memo[i1, i2] = max_len
            return max_len
        
        return dfs(0, 0)
            
        