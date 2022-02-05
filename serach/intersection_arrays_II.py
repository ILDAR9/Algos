from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        res = []
        for k, v in nums1.items():
            if k in nums2:
                res += [k] * min(nums1[k], nums2[k])
        return res


if __name__ == "__main__":
    inputs = [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4])
    ]
    outputs = [
        [2, 2],
        [9, 4]
    ]
    sol = Solution()
    for (nums1, nums2), expected in zip(inputs, outputs):
        res = sol.intersection(nums1, nums2)
        assert sorted(res) == sorted(expected), f"{res} while expected {expected}"
        print("pass")
