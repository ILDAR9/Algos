from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        for i, x in enumerate(reversed(nums[i+1:]), start=i+1):
            nums[i] = x


if __name__ == "__main__":
    inputs = [
        [5, 1, 1],
        [1, 1],
        [3, 2, 1],
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5]
    ]
    outputs = [
        [1, 1, 5],
        [1, 1],
        [1, 2, 3],
        [1, 3, 2],
        [1, 2, 3],
        [1, 5, 1]
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        sol.nextPermutation(nums)
        assert nums == expected, f"{nums} while expected {expected}"
        print("pass")
