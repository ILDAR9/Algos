from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        changed = False
        for i in range(n-1):
            if nums[i] <= nums[i+1]:
                continue
            if changed:
                return False
            if i == 0 or nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changed = True
        return True


if __name__ == "__main__":
    inputs = [
        [4,2,3],
        [4,2,1]
    ]
    outputs = [
        True,
        False
    ]

    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.checkPossibility(s)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')