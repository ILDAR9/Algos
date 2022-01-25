from typing import List
import sys


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        def bs(nums, target = None):
            start = 0
            end = len(nums)
            while start < end:
                mid = start + (end - 1 - start) // 2
                # print('start', start, 'mid', mid, 'end', end)
                if target is None:
                    if mid + 1 < end and nums[mid] < nums[mid+1]:
                        if nums[start] <= nums[mid]:
                            start = mid + 1
                        else:
                            end = mid
                    else:
                        return mid
                else:
                    if nums[mid] == target:
                        return mid
                    if target < nums[mid]:
                        end = mid
                    else:
                        start = mid+1
            return 0 if target is None else -1

        k = bs(nums)
        # print('k', k)
        if nums[k] == target:
            return k
        if target >= nums[0] and target < nums[k]:
            return bs(nums[:k+1], target = target)
        res = bs(nums[k+1:], target = target)
        return (k + 1 + res) if res >= 0 else  res
        


if __name__ == "__main__":
    inputs = [
        ([8,9,2,3,4], 9),
        ([5,1,3], 1),
        ([3,5,1], 3),
        ([1,3], 1),
        ([4,5,6,7,0,1,2], 0),
        ([4,5,6,7,0,1,2], 3),
        ([1], 0),
        ([-1], 0)
    ]
    outputs = [
        1, 1, 0, 0, 4, -1, -1, -1
    ]
    sol = Solution()
    for (nums, t), expected in zip(inputs, outputs):
        res = sol.search(nums, t)
        print('res', res)
        assert res == expected, f"{res} while expected {expected}"
