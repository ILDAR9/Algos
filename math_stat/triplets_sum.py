from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        seen = dict()
        dups = set()
        for i, target in enumerate(nums[:-2]):
            if i in dups:
                continue
            dups.add(i)
            for x in nums[i + 1: n]:
                complement = - target - x
                if complement in seen and seen[complement] == i:
                    ans.add(tuple(sorted((target, x, complement))))
                seen[x] = i

        return ans


if __name__ == "__main__":
    inputs = [
        [0, 0, 0, 0],
        [-1, 0, 1, 2, -1, -4],
        [],
        [0]
    ]
    outputs = [
        [[0, 0, 0]],
        [[-1, -1, 2], [-1, 0, 1]],
        [],
        []

    ]
    sol = Solution()
    for matrix, expected in zip(inputs, outputs):
        res = sol.threeSum(matrix)
        assert [list(row) for row in res] == expected, f'{res} while expected {expected}'
        print('pass')
