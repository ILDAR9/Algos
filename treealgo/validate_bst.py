from typing import Optional
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, leftval, rightval):
            if not root:
                return True
            if root.val <= leftval or root.val >= rightval:
                return False
            return dfs(root.left, leftval, root.val) and dfs(root.right, root.val, rightval)
        return dfs(root, -sys.maxsize, sys.maxsize)


if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [2, 1, 3],
        [5, 1, 4, None, None, 3, 6]
    ]
    expected_list = [
        True,
        False
    ]

    sol = Solution()
    for input_list, expected in zip(inputs, expected_list):
        if not input_list:
            root = None
        else:
            root = TreeNode(input_list[0])
            nodes = [root]
            for i, v in enumerate(input_list[1:], start=1):
                if not v:
                    continue
                node = TreeNode(v)
                parent_node = nodes[(i-1) // 2]
                if i % 2 == 1:
                    parent_node.left = node
                else:
                    parent_node.right = node
                nodes.append(node)

        res = sol.isValidBST(root)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
