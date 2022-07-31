from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
    	dp = dict()

    	def dfs(i: int, even: bool) -> int:
    		if i == len(nums):
    			return 0
    		if (i, even) in dp:
    			return dp[(i, even)]
    		val = nums[i] if even else -nums[i]
    		dp[(i, even)] = max(val + dfs(i+1, not even), dfs(i+1, even))
    		return dp[(i, even)]

    	return dfs(0, even=True)


if __name__ == "__main__":
	inputs = [
		[4,2,5,3],
		[5,6,7,8],
		[6,2,1,2,4,5]
	]
	outputs = [
		7,
		8,
		10
	]
	sol = Solution()
	for n, expected in zip(inputs, outputs):
		res = sol.maxAlternatingSum(n)
		assert res == expected, f"{res} while expected {expected}"
		print("pass")