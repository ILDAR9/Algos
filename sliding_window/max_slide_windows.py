from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass

if __name__ == "__main__":
    inputs = [
        ([1,3,-1,-3,5,3,6,7], 3),
        ([1], 1)
    ]
    outputs = [
        [3,3,5,5,6,7],
        [1]
    ]

    sol = Solution()
    for (nums, k), expected in zip(inputs, outputs):
        res = sol.maxSlidingWindow(nums, k)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')