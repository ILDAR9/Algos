from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        shifted = 1<<n

        return [[nums[i] for i, bit in enumerate(bin(i|shifted)[3:]) if bit == '1'] for
                    i in range(2**n)]

    def subsetsBacktrack(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, cur = []) -> None:
            nonlocal k, n

            if len(cur) == k:
                nonlocal outputs
                outputs.append(cur[:]) # copy of current subseq
                return
            
            for i in range(first, n):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()

        outputs = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return outputs



if __name__ == "__main__":
    inputs = [
        [1, 2, 3],
        [0]
    ]
    outputs = [
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        [[], [0]]
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.subsets(nums)
        assert sorted(res) == sorted(expected), f"{res} while expected {expected}"
#
