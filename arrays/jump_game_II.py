from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        n = len(nums)

        while r < n-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res += 1


        return res


if __name__ == "__main__":
    inputs = [
        [2,3,1,1,4],
        [2,3,0,1,4]
    ]
    outputs = [
        2,
        2
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.jump(nums)
        assert res == expected, f'{res} while expected {expected}'
        print('pass')