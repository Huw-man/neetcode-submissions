class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs.setdefault(n, 0)
            freqs[n] += 1
        
        return [n for n, v in sorted(freqs.items(), key=lambda x: -x[1])[:k]]