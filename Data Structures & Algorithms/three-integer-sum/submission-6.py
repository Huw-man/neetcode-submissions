class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        final = []

        for i in range(0, len(snums) - 2):
            if i > 0 and snums[i] == snums[i-1]:
                continue

            n = snums[i]
            j = i + 1
            k = len(snums) - 1
            while j < k:
                total = n + snums[j] + snums[k]
                if total == 0:
                    triple = [n, snums[j], snums[k]]
                    final.append(triple)
                    j += 1
                    k -= 1
                    while j < k and snums[j] == snums[j-1]:
                        j += 1
                    while j < k and snums[k] == snums[k+1]:
                        k -=1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return final
