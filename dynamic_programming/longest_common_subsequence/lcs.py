class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        # algo
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]



if __name__ == "__main__":
    inputs = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def")
    ]
    outputs = [
        3,
        3,
        0
    ]
    sol = Solution()
    for (text1, text2), expected in zip(inputs, outputs):
        res = sol.longestCommonSubsequence(text1, text2)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")