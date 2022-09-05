from typing import List
import random

class Solution:

	def __init__(self, w: List[int]):
		self.s = 0
		self.cums = []
		for n in w:
			self.s += n
			self.cums.append(self.s)
		self.cumlen = len(self.cums)

	def pickIndex(self) -> int:
		num = random.randint(1, self.s)
		return self.bin_search(num)

	def bin_search(self, num: int) -> int:
		l, r = 0, self.cumlen-1
		while l < r:
			mid = (l + r) // 2
			if self.cums[mid] < num:
				l = mid + 1
			else:
				r = mid
				
		return l


if __name__ == "__main__":
	inputs = [
		(["Solution","pickIndex"], [[[1]],[]]),
		(["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"], [[[1,3]],[],[],[],[],[]] )
	]
	outputs = [
		[None,0],
		[None,1,1,1,1,0]
	]

	for (ops, nums), expected in zip(inputs, outputs):
		res = []
		for op, num_list in zip(ops, nums):
			val = None
			if op == 'Solution':
				num_list = num_list[0]
				obj = Solution(num_list)
			else:
				val = obj.pickIndex()
			res.append(val)
		assert res == expected, f"{res} while expected {expected}"
		print('pass')