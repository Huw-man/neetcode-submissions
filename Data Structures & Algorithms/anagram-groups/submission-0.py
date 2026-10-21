class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for sl in strs:
            groups.setdefault(tuple(self.getCount(sl)), []).append(sl)
        return [g for g in groups.values()]

    def getCount(self, s: str) -> List[int]:
        counts = [0] * 26
        for a in s:
            counts[ord(a) - 97] += 1

        return counts
