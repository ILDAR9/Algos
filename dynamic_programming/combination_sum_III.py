from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()

        def backtract(nums):
            if len(nums) == k:
                if sum(nums) == n:
                    res.add(tuple(sorted(nums)))
                return
            if sum(nums) >= n:
                return
            for i in range(1, 10):
                if i in nums:
                    continue
                nums.append(i)
                backtract(nums)
                nums.pop()
            return
        backtract(nums=[])
        return res


if __name__ == "__main__":
    inputs = [
        (3, 7),
        (3, 9),
        (4, 1),
    ]
    outputs = [
        [[1, 2, 4]],
        [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
        []
    ]
    sol = Solution()
    for (k, n), expected in zip(inputs, outputs):
        res = sol.combinationSum3(k, n)
        res = sorted(map(list, res))
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
