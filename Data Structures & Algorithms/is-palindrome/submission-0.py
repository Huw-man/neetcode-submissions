class Solution:
    def isPalindrome(self, s: str) -> bool:
        strippedp = []
        for c in s:
            if c.isalnum():
                strippedp.append(c.lower())
        lowerp = "".join(strippedp)
        return lowerp == lowerp[::-1]