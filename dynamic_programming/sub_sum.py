from typing import List
import functools


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        s = 0
        cash = {0: 1}  # num & occurence
        for start in range(n):
            s += nums[start]
            if s - k in cash:
                count += cash[s-k]
            cash[s] = cash.get(s, 0) + 1
        return count


if __name__ == "__main__":
    inputs = [
        ([1], 0),
        ([0], 0),
        ([1, 2, 1, 2, 1], 3),
        ([1, 1, 1], 2),
        ([1, 2, 3], 3)
    ]
    outputs = [
        0,
        1,
        4,
        2,
        2
    ]
    sol = Solution()
    for (nums, k), expected in zip(inputs, outputs):
        res = sol.subarraySum(nums, k)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
