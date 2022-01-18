from typing import List
import sys


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(sub, start=0):
            if not sub:
                return
            split = len(sub) // 2
            # print('start', start, 'split', split, sub)
            if sub[split] < target:
                bs(sub[split+1:], start + split + 1)
            elif sub[split] > target:
                bs(sub[:split], start)
            else:
                if split > 0 and sub[split - 1] == target:
                    bs(sub[:split], start)
                elif split < len(sub)-1 and sub[split+1] == target:
                    bs(sub[split+1:], start + split + 1)
                else:
                    nonlocal min_i, max_i
                    min_i = min(start + split, min_i)
                    max_i = max(start + split, max_i)

        nlen = len(nums)
        min_i = nlen
        max_i = -1
        bs(nums)
        return [min_i if min_i < nlen else -1, max_i]


if __name__ == "__main__":
    inputs = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6),
        ([5, 7, 7, 8, 8, 10], 5),
        ([], 0)
    ]
    outputs = [
        [3, 4],
        [-1, -1],
        [0, 0],
        [-1, -1],
    ]
    sol = Solution()
    for (nums, t), expected in zip(inputs, outputs):
        res = sol.searchRange(nums, t)
        print('res', res)
        assert res == expected, f"{res} while expected {expected}"
