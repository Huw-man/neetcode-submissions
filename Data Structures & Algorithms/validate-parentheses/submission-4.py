class Solution:
    def isValid(self, s: str) -> bool:
        sl = list(s)
        stk = []
        match = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in ['(', '{', '[']:
                stk.append(c)
            elif stk and match[c] != stk[-1]:
                return False
            elif not stk:
                return False
            else:
                stk.pop()
        return not stk
       