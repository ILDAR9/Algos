from typing import Optional, Tuple

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = self.right = None

	def __repr__(self):
		if not self.left and not self.right:
			return f"val={self.val}"
		return f"val={self.val}, ({self.left}, {self.right})"

class Solution:
	"""
	0 <= num < 10
	"""

	def str2tree(self, s: str) -> Optional[TreeNode]:
		if not s:
			return None

		def dfs(i: int) -> Tuple[TreeNode, int]:
			node = TreeNode(s[i])
			i+=1

			# left open
			if i< len(s) and s[i] == '(':
				i+=1
				node.left, i = dfs(i)
				i+=1

			# right open
			if i < len(s) and s[i] == '(':
				i+=1
				node.right, i = dfs(i)
				i+=1
			return node, i


		root, i = dfs(0)
		return root


if __name__ == "__main__":
    inputs = [
    	"5(2)()",
    	"5(4(2)(3))(6()(7))",
        "4(2(3)(1))(6(5))",
    ]
    sol = Solution()
    for s in inputs:
        output = sol.str2tree(s)
        print('expect:', s)
        print(output)
        print()
