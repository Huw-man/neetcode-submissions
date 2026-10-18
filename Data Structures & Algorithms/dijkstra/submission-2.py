import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        visited = set()
        neighbors = []
        heapq.heappush(neighbors, (0, src))
        distances = {}
        while neighbors:
            cw, curr = heapq.heappop(neighbors)
            if curr in visited:
                continue
            
            for curr, next_n, next_w in filter(lambda e: e[0] == curr, edges):
                if next_n in visited:
                    continue
                heapq.heappush(neighbors, (cw + next_w, next_n))
            
            distances[curr] = cw
            visited.add(curr)

        # add unreachable vertices
        for i in range(n):
            if i not in distances:
                distances[i] = -1
        return distances