class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        c_set = {}
        for r in range(len(s)):
            if s[r] not in c_set:
                c_set[s[r]] = 0
            c_set[s[r]] +=1

            while (r-l+1) - max(c_set.values()) > k:
                c_set[s[l]] -=1
                l += 1
            max_len = max(max_len, r - l +1)
        return max_len