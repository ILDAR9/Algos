class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] * m

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

    def __init__(self):
        self.memory = dict()

    def uniquePathsRec(self, m: int, n: int) -> int:
        k = (m,n)
        v = self.memory.get(k, None)
        if v:
            return v
        if m == 1 or n == 1:
            return 1
        v = self.uniquePathsRec(m-1, n) + self.uniquePathsRec(m, n-1)
        self.memory[k] = v
        return v


if __name__ == "__main__":
    inputs = [
        (3, 2),
        (3, 7)
    ]
    outputs = [
        3,
        28
    ]
    sol = Solution()
    for (m, n), expected in zip(inputs, outputs):
        res = sol.uniquePaths(m, n)
        print('res', res)
        assert res == expected, f"{res} while expected {expected}"
