from typing import List


class Solution:
    """ Longest Increasing Subsequence"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp: List[int] = [1] * len(nums)
        maxans = 1
        for i in range(1, len(nums)):
            maxval = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
        return maxans


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # Output: 4
    res = Solution().lengthOfLIS(nums)
    print(f"Res: '{res}'")
