class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = [0]*26, [0]*26
        for a in s:
            count_s[(ord(a)-97)] += 1
        for b in t:
            count_t[ord(b) -97] += 1
        
        for i, v in enumerate(count_s):
            if v != count_t[i]:
                return False
        return True