from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lnums = [1] * n
        for i in range(1, n):
            lnums[i] = nums[i-1] * lnums[i-1]
        r = 1
        for i in range(n-1, -1, -1):
            lnums[i] = lnums[i] * r
            r *= nums[i]
        return lnums


if __name__ == "__main__":
    inputs = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3]
    ]
    outputs = [
        [24, 12, 8, 6],
        [0, 0, 9, 0, 0]
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.productExceptSelf(nums)
        assert sorted(res) == sorted(expected), f"{res} while expected {expected}"
        print("pass")
