from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = dict() # (index, count combinations)

        def backtrack(i, total):
            if i == len(nums):
                return int(total == target)
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])
            return dp[(i, total)]

        return backtrack(0, 0)

if __name__ == "__main__":
    inputs = [
        ([1,1,1,1,1], 3),
        ([1], 1)
    ]
    outputs = [
        5,
        1
    ]
    sol = Solution()
    for (nums, target), expected in zip(inputs, outputs):
        res = sol.findTargetSumWays(nums, target)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")