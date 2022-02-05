from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    inputs = [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4])
    ]
    outputs = [
        [2],
        [9, 4]
    ]
    sol = Solution()
    for (nums1, nums2), expected in zip(inputs, outputs):
        res = sol.intersection(nums1, nums2)
        assert sorted(res) == sorted(expected), f"{res} while expected {expected}"
        print("pass")
