class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        offset = 1
        while offset < n/2:
            offset *=2
        return 1 + self.hammingWeight(n % offset)
        