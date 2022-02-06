from typing import List


class Solution:
    # fewest number of coins
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_non_real = amount + 1
        dp = [0] + [max_non_real] * amount
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        return dp[-1] if dp[-1] != max_non_real else -1


if __name__ == "__main__":
    inputs = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0)
    ]
    outputs = [
        3,
        -1,
        0
    ]
    sol = Solution()
    for (coins, amount), expected in zip(inputs, outputs):
        res = sol.coinChange(coins, amount)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
