from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxarea = 0
        while left < right:
            hl = height[left]
            hr = height[right]
            area = (right - left) * min(hl, hr)
            maxarea = max(maxarea, area)
            if hr < hl:
                right -= 1
            else:
                left += 1

        return maxarea


if __name__ == "__main__":
    inputs = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1]
    ]
    outputs = [
        49,
        1
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.maxArea(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
