from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    inputs = [
        [1,2,0],
        [3,4,-1,1],
        [7,8,9,11,12]
    ]
    expected_list = [
        3,
        2,
        1
    ]
    sol = Solution()
    for nums, expected in zip(inputs, expected_list):
        output = sol.firstMissingPositive(nums)
        assert output == expected, f'{output} while expected {expected}'
        print("pass")