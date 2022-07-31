from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # edge cases
        if sum(nums) % 2:
            return False
        # prerequisites
        target = sum(nums) // 2
        dp = {0}
        for n in nums:
            new_dp = dp.copy()
            for t in dp:
                new_dp.add(t+n)
            dp = new_dp
        return target in dp




if __name__ == "__main__":
    inputs = [
        [1,5,11,5],
        [1,2,3,5]
    ]
    outputs = [
        True,
        False
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.canPartition(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")