class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        final = []
        f_set = set()

        for i in range(0, len(snums) - 2):
            n = snums[i]
            j = i + 1
            k = len(snums) - 1
            while j < k:
                f_sum = snums[j] + snums[k]
                if f_sum + n == 0:
                    triple = [n, snums[j], snums[k]]
                    if tuple(triple) not in f_set:
                        final.append(triple)
                    f_set.add(tuple(triple))
                    j += 1
                elif f_sum + n > 0:
                    # decrease f_sum
                    k -= 1
                elif f_sum + n < 0:
                    # increase f_sum
                    j += 1
        return final
