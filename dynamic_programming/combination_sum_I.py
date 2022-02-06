from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(nums: List[int], remain: int, start: int) -> None:
            if remain <= 0:
                if remain == 0:
                    res.append(nums[:])
                return
            for i in range(start, len(candidates)):
                x = candidates[i]
                nums.append(x)
                backtrack(nums, remain - x, i)
                nums.pop()
            return

        backtrack(nums=[], remain=target, start=0)
        return res


if __name__ == "__main__":
    inputs = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1)
    ]
    outputs = [
        [[2, 2, 3], [7]],
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        []
    ]
    sol = Solution()
    for (candidates, target), expected in zip(inputs, outputs):
        res = sol.combinationSum(candidates, target)
        expected = sorted(expected)
        res = sorted(map(list, res))
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
