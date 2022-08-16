from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l = 0
        r = len(A) - 1
        while True:
            # median in A
            i = (l+r) // 2
            # median in B
            j = half - i
            #correction
            j-=2

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i+1] if i+1 < len(A) else float('infinity')
            Bleft = B[j] if j>=0 else float('-infinity')
            Bright = B[j+1] if j+1 < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1




if __name__ == "__main__":
    inputs = [
        ([1,3], [2]),
        ([1,2], [3,4])
    ]
    expected_list = [
        2.00000,
        2.50000
    ]
    sol = Solution()
    for (deadends, target), expected in zip(inputs, expected_list):
        output = sol.findMedianSortedArrays(deadends, target)
        assert output == expected, f'{output} while expected {expected}'
        print("pass")
        