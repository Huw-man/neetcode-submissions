class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count

    def hammingWeight1(self, n: int) -> int:
        if n == 0:
            return 0
        offset = 1
        while offset * 2 < n:
            offset *=2
        return 1 + self.hammingWeight(n % offset)
        