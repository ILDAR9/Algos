from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l, r = 0, 0
        queue = deque()
        res: List[int] = [] # index store

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if queue and l > queue[0]:
                queue.popleft()

            if r + 1 >= k:
                res.append(nums[queue[0]])
                l += 1
            r+=1

        return res


if __name__ == "__main__":
    inputs = [
        ([1,3,1,2,0,5], 3),
        ([1,3,-1,-3,5,3,6,7], 3),
        ([1], 1)
    ]
    outputs = [
        [3,3,2,5],
        [3,3,5,5,6,7],
        [1]
    ]

    sol = Solution()
    for (nums, k), expected in zip(inputs, outputs):
        res = sol.maxSlidingWindow(nums, k)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')