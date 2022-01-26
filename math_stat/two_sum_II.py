from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, x in enumerate(nums):
            if x in d:
                return [d[x]+1, i+1]
            d[target - x] = i
        return []


if __name__ == "__main__":
    inputs = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1)
    ]
    outputs = [
        [1, 2],
        [1, 3],
        [1, 2]
    ]
    sol = Solution()
    for (arr, target), expected in zip(inputs, outputs):
        res = sol.twoSum(arr, target)
        assert res == expected, f'{res} while expected {expected}'
        print('pass')
