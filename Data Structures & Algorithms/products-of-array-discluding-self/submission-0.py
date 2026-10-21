class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # cumulative product forward
        cp_f = [nums[0]]*len(nums)
        for i, n in enumerate(nums):
            if i-1 >= 0:
                cp_f[i] = cp_f[i-1]*n
        
        # cumulative product reverse
        cp_r = [nums[-1]]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            n = nums[i] 
            if i+1 <= len(nums)-1:
                cp_r[i] = cp_r[i+1]*n

        final = [0]*len(nums)
        for i, n in enumerate(nums):
            if i == len(nums) -1:
                final[i] = cp_f[i-1]
            elif i == 0:
                final[i] = cp_r[1]
            else:
                final[i] = cp_f[i-1] * cp_r[i+1]
        return final
            