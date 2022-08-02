from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            count = 0
            for v in Counter(nums).values():
                if v > 1:
                    count += 1
            return count
        count = 0
        nums = set(nums)
        for x in nums:
            if x+k in nums:
                count += 1
        return count


if __name__ == "__main__":
    inputs = [
        ([3, 1, 4, 1, 5], 2),
        ([1, 2, 3, 4, 5], 1),
        ([1, 3, 1, 5, 4], 0)
    ]
    outputs = [
        2,
        4,
        1
    ]
    sol = Solution()
    for (nums, k), expected in zip(inputs, outputs):
        res = sol.findPairs(nums, k)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
