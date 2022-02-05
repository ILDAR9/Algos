from typing import List
import sys


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_far = nums[0]
        min_far = nums[0]
        result = max_far
        for cur in nums[1:]:

            tempmax = max(cur * max_far, cur, cur * min_far)
            min_far = min(cur * min_far, cur, cur * max_far)
            max_far = tempmax
            result = max(max_far, result)

        return result


if __name__ == "__main__":
    inputs = [
        [-3, -1, -1],
        [2, 3, -2, 4],
        [-2, 0, -1]
    ]
    outputs = [
        3,
        6,
        0
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.maxProduct(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
