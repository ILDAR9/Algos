
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node) -> int:
            if node == None:
                return 0

            leftedges = dfs(node.left)
            rightedges = dfs(node.right)
            dhat = leftedges + rightedges
            nonlocal diameter
            if dhat > diameter:
                diameter = dhat
            return max(leftedges, rightedges) + 1

        diameter = 0
        dfs(root)
        return diameter


if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [1, 2, 3, 4, 5],
        [1, 2]
    ]
    expected_list = [
        3,
        1
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

        res = sol.diameterOfBinaryTree(root)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
