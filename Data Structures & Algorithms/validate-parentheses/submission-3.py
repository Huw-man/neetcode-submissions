class Solution:
    def isValid(self, s: str) -> bool:
        sl = list(s)
        stk = []
        match = {')':'(', '}':'{', ']':'['}
        for c in s:
            print(stk)
            if c in ['(', '{', '[']:
                stk.append(c)
            elif stk:
                if match[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                return False
        return not stk
       