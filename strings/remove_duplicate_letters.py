class Solution:
	def removeDuplicateLetters(self, s: str) -> str:
		last_occur = {c:i for i,c in enumerate(s)}

		visited = set()
		stack = []
		for i, c in enumerate(s):
			if c in visited:
				continue
			while stack and last_occur[stack[-1]] > i and stack[-1] > c:
				visited.remove(stack.pop())
			visited.add(c)
			stack.append(c)
		return ''.join(stack)


if __name__ == "__main__":
	inputs = [
		"bcabc",
		"cdadabcc",
		"bcabc",
		"cbacdcbc",
	]
	outputs = [
		"abc",
		"adbc",
		"abc",
		"acdb"
	]
	sol = Solution()
	for s, expected in zip(inputs, outputs):
		res = sol.removeDuplicateLetters(s)
		assert res == expected, f"{res} while expected {expected}"
		print("pass")	