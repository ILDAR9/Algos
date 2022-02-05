from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= num ^ i
        return missing


if __name__ == "__main__":
    inputs = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1]
    ]
    outputs = [
        2,
        2,
        8
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.missingNumber(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
