from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        is_changed = False
        for i in range(len(nums)-1):
            if nums[i+1] >= nums[i]:
                continue
            if is_changed:
                return False

            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            is_changed = True
        return True



if __name__ == "__main__":
    inputs = [
        [4,2,3],
        [4,2,1],
        [3,4,2,3]
    ]
    outputs = [
        True,
        False,
        False
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.checkPossibility(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
