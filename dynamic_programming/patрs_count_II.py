class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n] * m
        dp[0] = [0 if x else 1 for x in obstacleGrid[0]]
        for i in range(m):
            dp[i][0] = 0 if obstacleGrid[i][0] else 1
        print('dp', dp)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:    
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


if __name__ == "__main__":
    inputs = [
        [[0,0],[1,1],[0,0]],
        [[0,0,0],[0,1,0],[0,0,0]],
        [[0,1],[0,0]],
        [[1,0]],
    ]
    outputs = [
        0,
        2,
        1,
        0,
    ]
    sol = Solution()
    for obstacleGrid, expected in zip(inputs, outputs):
        res = sol.uniquePathsWithObstacles(obstacleGrid)
        print('res', res)
        assert res == expected, f"{res} while expected {expected}"
