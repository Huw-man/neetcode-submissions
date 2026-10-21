class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset = {}
        for n in nums:
            if n not in nset:
                nset[n] = 1
            else:
                return True
        return False