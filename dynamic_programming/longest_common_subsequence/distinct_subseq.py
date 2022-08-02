class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = dict()

        def dfs(i, j) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            k = (i,j) 
            if k in dp:
                return dp[k]
            if s[i] == t[j]:
                dp[k] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                dp[k] = dfs(i+1, j)
            return dp[k]

        return dfs(0,0)


if __name__ == "__main__":
    inputs = [
        ("rabbbit", "rabbit"),
        ("babgbag", "bag")
    ]
    outputs = [
        3,
        5
    ]
    sol = Solution()
    for (text1, text2), expected in zip(inputs, outputs):
        res = sol.numDistinct(text1, text2)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")