from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * (amount)
        for x in coins:
            for curamount in range(1, amount+1):
                if curamount - x >= 0:
                    dp[curamount] += dp[curamount-x]
        return dp[-1]


if __name__ == "__main__":
    inputs = [
        (5, [1, 2, 5]),
        (3, [2]),
        (10, [10])
    ]
    outputs = [
        4,
        0,
        1
    ]
    sol = Solution()
    for (amount, coins), expected in zip(inputs, outputs):
        res = sol.change(amount, coins)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
