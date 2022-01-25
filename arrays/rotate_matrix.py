from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]


if __name__ == "__main__":
    inputs = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    ]
    outputs = [
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    ]
    sol = Solution()
    for matrix, expected in zip(inputs, outputs):
        sol.rotate(matrix)
        assert matrix == expected, f'{matrix} while expected {expected}'
        print('pass')
