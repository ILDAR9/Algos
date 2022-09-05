from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bin_search(is_left_biased: bool) -> int:
            l, r = 0, len(nums) - 1

            res = -1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    res = mid
                    if is_left_biased:
                        r = mid-1
                    else:
                        l = mid+1
            return res


        left = bin_search(True)
        right = bin_search(False)
        return [left, right]

        

if __name__ == "__main__":
    inputs = [
        ([5,7,7,8,8,10], 8),
        ([5,7,7,8,8,10], 6),
        ([], 0)
    ]
    outputs = [
        [3,4],
        [-1,-1],
        [-1,-1]
    ]

    sol = Solution()
    for (nums, target), expected in zip(inputs, outputs):
        res = sol.searchRange(nums, target)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')