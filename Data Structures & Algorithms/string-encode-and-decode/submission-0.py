class Solution:

    def encode(self, strs: List[str]) -> str:
        final = []
        for s in strs:
            final.append(str(len(s)) + '#' + s)
        return "".join(final)


    def decode(self, s: str) -> List[str]:
        i = 0
        final = []
        while i < len(s):
            h_i = i
            while s[h_i] != '#':
                h_i +=1
            # decode word
            length = int(s[i:h_i])
            final.append(s[h_i+1:h_i+1+length])
            i = h_i + 1 + length
        return final