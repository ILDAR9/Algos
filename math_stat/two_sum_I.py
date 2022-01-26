from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, x in enumerate(nums):
            if x in d:
                return [d[x], i]
            d[target - x] = i
        return []


if __name__ == "__main__":
    inputs = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]
    outputs = [
        [0, 1],
        [1, 2],
        [0, 1]
    ]
    sol = Solution()
    for (arr, target), expected in zip(inputs, outputs):
        res = sol.twoSum(arr, target)
        assert res == expected, f'{res} while expected {expected}'
        print('pass')
