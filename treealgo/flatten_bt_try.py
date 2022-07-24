from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # return str(self.val)
        return f"[{self.val}, l={self.left}, r={self.right}]"

class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return None
            left_tail = dfs(root.left)
            right_tail = dfs(root.right)

            if root.left:
                left_tail.right = root.right
                root.right = root.left
                root.left = None

            # returns tails
            return right_tail or left_tail or root

        dfs(root)

if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [1,2,5,3,4,None,6],
        [],
        [0],
        [100, 50, 200, 25, 75, 125, 350, None, 30, 60]
    ]
    expected_list = [
        [1,None,2,None,3,None,4,None,5,None,6],
        [],
        [0],
        [25, None, 30, None, 50, None, 60, None, 73, None, 100, None, 125, None, 200, None, 350]
    ]


    for input_list, expected in zip(inputs, expected_list):
        if not input_list:
            root = None
        else:
            root = TreeNode(input_list[0])
            nodes = [root]
            for i, v in enumerate(input_list[1:], start = 1):
                node = TreeNode(v)
                parent_node = nodes[(i-1) // 2]
                if i % 2 == 1:
                    parent_node.left = node
                else:
                    parent_node.right = node
                nodes.append(node)

        print(root)
        sol = Solution()
        res = sol.flatten(root)
        # assert res == expected, res
        print()
        print(root)
        print('----------')