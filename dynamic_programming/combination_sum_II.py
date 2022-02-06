from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(nums: List[int], remain: int, start: int) -> None:
            if remain <= 0 or start == len(candidates):
                if remain == 0:
                    res.append(nums[:])  # copy
                return
            i = start
            for i in range(start, len(candidates)):
                x = candidates[i]
                if i > start and x == candidates[i-1]:
                    continue
                nums.append(x)
                backtrack(nums, remain - x, i+1)
                nums.pop()
        backtrack([], target, 0)
        return res


if __name__ == "__main__":
    inputs = [
        ([10, 1, 2, 7, 6, 1, 5], 8),
        ([2, 5, 2, 1, 2], 5),
        ([3,1,3,5,1,1], 8)
    ]
    outputs = [
        [
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ],
        [
            [1, 2, 2],
            [5]
        ],
        [[1,1,1,5],[1,1,3,3],[3,5]]
    ]
    sol = Solution()
    for (candidates, target), expected in zip(inputs, outputs):
        res = sol.combinationSum2(candidates, target)
        expected = sorted(expected)
        res = sorted(map(list, res))
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
