class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][n-1]


if __name__ == "__main__":
    inputs = [
        "zzazz",
        "mbadm",
        "leetcode"
    ]
    outputs = [
        0,
        2,
        5
    ]

    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.minInsertions(s)
        assert res == expected, res
        print('pass')
