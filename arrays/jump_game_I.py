from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        goal_idx = n - 1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= goal_idx:
                goal_idx = i
        return goal_idx == 0


if __name__ == "__main__":
    inputs = [
        [2,3,1,1,4],
        [3,2,1,0,4]
    ]
    outputs = [
        True,
        False
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.canJump(nums)
        assert res == expected, f'{res} while expected {expected}'
        print('pass')