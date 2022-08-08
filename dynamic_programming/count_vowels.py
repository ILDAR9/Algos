class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        a -> e
        e - > a i
        i -> a e o u
        o -> i u
        u -> a

        INVERS
        a <- e i u
        e <- a i
        i <- e o
        o <- i
        u <- i o
        """
        POWER=5
        # [level, letter] -> count
        dp = [[0] * POWER, [1,1,1,1,1]]
        a = 0
        e = 1
        i = 2
        o = 3
        u = 4

        mod = 10**9 + 7

        for j in range(2, n+1):
            dp.append([0] * POWER)
            prev_i = j-1
            dp[j][a] = dp[prev_i][e] + dp[prev_i][i] + dp[prev_i][u] % mod
            dp[j][e] = dp[prev_i][a] + dp[prev_i][i] % mod
            dp[j][i] = dp[prev_i][e] + dp[prev_i][o] % mod
            dp[j][o] = dp[prev_i][i] % mod
            dp[j][u] = dp[prev_i][i] + dp[prev_i][o]  % mod

        return sum(dp[n]) % mod


if __name__ == "__main__":
    inputs = [
        144,
        1,
        2,
        5
    ]
    outputs = [
        18208803,
        5,
        10,
        68
    ]
    sol = Solution()
    for n, expected in zip(inputs, outputs):
        res = sol.countVowelPermutation(n)
        assert res == expected, f"{res} while expected {expected}"
