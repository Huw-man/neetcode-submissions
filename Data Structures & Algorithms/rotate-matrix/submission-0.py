class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose
        for j in range(len(matrix)):
            for i in range(j):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        # reverse rows
        for r in range(len(matrix)):
            matrix[r] = matrix[r][::-1]