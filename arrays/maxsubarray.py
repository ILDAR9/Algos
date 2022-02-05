from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = max(nums[0], 0)
        maxsub = nums[0]
        for x in nums[1:]:
            cur += x
            maxsub = max(maxsub, cur)
            if cur <= 0:
                cur = 0
        return maxsub


if __name__ == "__main__":
    inputs = [
        [-1],
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8]
    ]
    outputs = [
        -1,
        6,
        1,
        23
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.maxSubArray(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
