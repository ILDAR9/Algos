from typing import List

class Solution:
	def rob(self, nums: List[int]) -> int:
		n = len(nums)
		if n == 1:
			return nums[0]
		one = nums[0]
		two = max(nums[:2])
		for x in nums[2:]:
			temp = two
			two = max(two, one+x)
			one = temp
		return two


if __name__ == "__main__":
	inputs = [
		[2,1],
		[1,2,3,1],
		[2,7,9,3,1]
	]
	outputs = [
		2,
		4,
		12
	]
	sol = Solution()
	for n, expected in zip(inputs, outputs):
		res = sol.rob(n)
		assert res == expected, f"{res} while expected {expected}"
		print("pass")