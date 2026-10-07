# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        results = []
        for i, p in enumerate(pairs):
            for j in range(i):
                if p.key < pairs[j].key:
                    pp = pairs.pop(i)
                    pairs.insert(j, pp)
                    break
            
            results.append(pairs[:])
        return results
            
                
    
         
        