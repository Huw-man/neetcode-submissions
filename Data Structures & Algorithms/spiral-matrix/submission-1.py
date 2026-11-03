class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        x, y, dx, dy = -1, 0, 1, 0
        steps = n
        other = m

        while steps > 0:
            for i in range(steps):
                x += dx
                y += dy
                res.append(matrix[y][x])
            steps, other = other -1, steps 
            dx, dy = -dy, dx
        
        return res


    def spiralOrderRecursive(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        def row_dir(n, m):
            if n <= 0 or m <= 0:
                return
            for _ in range(n):
                yield (1, 0)
            for dx, dy in row_dir(m-1, n):
                yield (-dy, dx)
                
        res = []
        sx, sy = -1, 0
        for dx, dy in row_dir(n, m):
            sx += dx
            sy += dy
            res.append(matrix[sy][sx])
            
        return res
