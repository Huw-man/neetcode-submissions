class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, j):
            if i >= len(nums):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            # skip
            max_len = dfs(i+1, j)

            if nums[i] > nums[j] or j == -1:
                max_len = max(1 + dfs(i+1, i), max_len) 
            memo[(i, j)] = max_len
            return max_len
        
        return dfs(0, -1)

        