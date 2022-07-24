from typing import List, Tuple

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # prev & min stack
        stack: List[Tuple] = []
        cur_min = nums[0]

        for n in nums[1:]:
            # valid j & k search
            while stack and n >= stack[-1][0]:
                stack.pop()
            # if exists valid j & k and there's valid i
            if stack and stack[-1][1] < n:
                return True
            # update j and i
            stack.append((n, cur_min))
            cur_min = min(cur_min, n)
        return False


if __name__ == "__main__":
    inputs = [
        [1,2,3,4],
        [3,1,4,2],
        [-1,3,2,0]
    ]
    outputs = [
        False,
        True,
        True
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.find132pattern(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
