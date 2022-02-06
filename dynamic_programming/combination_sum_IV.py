from typing import List
from functools import lru_cache


class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for cursum in range(1, target + 1):
            for x in nums:
                if cursum - x >= 0:
                    dp[cursum] += dp[cursum - x]
        return dp[-1]

    def combinationSum4TopDown(self, nums: List[int], target: int) -> int:
        nums.sort()

        @lru_cache(None)
        def dp(remain):

            if remain == 0:
                return 1

            count = 0
            for x in nums:
                if remain - x >= 0:
                    count += dp(remain-x)
                else:
                    break
            return count

        return dp(target)


if __name__ == "__main__":
    inputs = [
        ([3, 1, 2, 4], 4),
        ([4, 2, 1], 32),
        ([1, 2, 3], 4),
        ([9], 3)
    ]
    outputs = [
        8,
        39882198,
        7,
        0
    ]
    sol = Solution()
    for (nums, target), expected in zip(inputs, outputs):
        res = sol.combinationSum4(nums, target)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
