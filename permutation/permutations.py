from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
        	return [nums[:]]

        result = []

        for i in range(len(nums)):
	        x = nums.pop(0)

	        perms = self.permute(nums)
	        for perm in perms:
	        	perm.append(x)
	        result.extend(perms)
	        nums.append(x)

        return result

if __name__ == "__main__":
    inputs = [
        [1,2,3],
        [0,1],
        [1]
    ]
    outputs = [
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
        [[0,1],[1,0]],
        [[1]]
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.permute(nums)
        assert sorted(res) == sorted(expected), f"{res} while expected {expected}"
        print("pass")