class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        c_set = set()
        for r in range(len(s)):
            while s[r] in c_set:
                c_set.remove(s[l])
                l +=1
            max_len = max(max_len, r - l + 1)
            c_set.add(s[r])
        return max_len
            
