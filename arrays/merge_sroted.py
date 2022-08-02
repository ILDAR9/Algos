from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1,  n-1
        while j >= 0:
            idx = i+j+1
            if i >= 0 and nums1[i] >= nums2[j]:
                x = nums1[i]
                i -= 1
            else:
                x = nums2[j]
                j -= 1
            nums1[idx] = x


"""
[1,2,5,  0, 0, 0] [2,3,4]

1,2,2,0,0,0  5,3,4
"""

if __name__ == "__main__":
    inputs = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        ([1], 1, [], 0),
        ([0], 0, [1], 1)
    ]
    outputs = [
        [1, 2, 2, 3, 5, 6],
        [1],
        [1]
    ]
    sol = Solution()
    for (nums1, m, nums2, n), expected in zip(inputs, outputs):
        sol.merge(nums1, m, nums2, n)
        assert nums1 == expected, f'{nums1} while expected {expected}'
        print('pass')
