from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        check = lambda idx: nums[idx] < nums[idx - 1 if idx >= 1 else n-1]

        def bin_search(start, end):
            if end < start:
                return 0
            if check(start):
                return start
            if check(end):
                return end
            mid = start + (end - start) // 2
            if check(mid):
                return mid
            if nums[start] > nums[mid]:
                return bin_search(start, mid-1)
                
            else:
                return bin_search(mid+1, end)


        residx = bin_search(0, n - 1)
        return nums[residx]


if __name__ == "__main__":
    inputs = [
        [3],
        [5,1,2,3,4],
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17]
    ]
    outputs = [
        3,
        1,
        1,
        0,
        11
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.findMin(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
