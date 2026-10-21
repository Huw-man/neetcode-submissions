class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0

        starts = []
        for i in nums:
            if i-1 not in nset:
                starts.append(i)

        for s in starts:
            c = s
            j = 0
            while c+1 in nset:
                c += 1
                j += 1
            longest = max(longest, j+1)
        return longest


        