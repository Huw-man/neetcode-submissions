class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)

        offset = 1
        for i in range(1, n+1):
            print(i, offset)
            if offset*2 == i:
                offset = offset*2
            res[i] = 1 + res[i - offset]
        return res

        
        