from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = [nums[0]]
        for x in nums[1:]:
            if x > res[-1]:
                res.append(x)
            else:
                for i, y in enumerate(res):
                    if y >= x:
                        res[i] = x
                        break

        return len(res)


if __name__ == "__main__":
    inputs = [
        [4,10,4,3,8,9],
        [10,9,2,5,3,7,101,18],
        [0,1,0,3,2,3],
        [7,7,7,7,7,7,7]
    ]
    outputs = [
        3,
        4,
        4,
        1
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.lengthOfLIS(nums)
        print('res', res)
        assert res == expected, f"{res} while expected {expected}"
