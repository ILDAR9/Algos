from typing import List


class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        START = 1
        END = 2
        EMPTY = 0
        OBSTACLE = -1
        VISITED = 3
        n = len(grid)
        m = len(grid[0])

        four_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(i: int, j: int, remain: int) -> None:
            if grid[i][j] == END:
                if remain == 1:
                    nonlocal num_paths
                    num_paths += 1
                return
            
            # mark visited
            grid[i][j] = VISITED
            for hop_i, hop_j in four_directions:
                i_hat = i + hop_i
                j_hat = j + hop_j
                if i_hat >= 0 and i_hat < n and j_hat >= 0 and j_hat < m and grid[i_hat][j_hat] != OBSTACLE and grid[i_hat][j_hat] != VISITED:
                    backtrack(i_hat, j_hat, remain - 1)

            # unmark visited
            grid[i][j] = EMPTY

        # Counter non-obstacle cells
        num_nonobs = 0
        start_i, start_j = 0, 0
        for i in range(n):
            for j in range(m):
                cell = grid[i][j]
                if cell == OBSTACLE:
                    continue
                if cell == START:
                    start_i = i
                    start_j = j
                num_nonobs += 1

        # Count pats cover all cells
        num_paths = 0
        backtrack(start_i, start_j, remain=num_nonobs)
        return num_paths


if __name__ == "__main__":
    inputs = [
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]],
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]],
        [[0, 1], [2, 0]]
    ]
    outputs = [
        2,
        4,
        0
    ]
    sol = Solution()
    for obstacleGrid, expected in zip(inputs, outputs):
        res = sol.uniquePathsIII(obstacleGrid)
        print('res', res)
        assert res == expected, f"{res} while expected {expected}"
