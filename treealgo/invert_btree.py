from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [4,2,7,1,3,6,9],
        [2,1,3],
        []
    ]
    expected_list = [
        [4,7,2,9,6,3,1],
        [2,3,1],
        []
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

        sol = Solution()
        res = sol.invertTree(root)
        print()
        print(root)
        print('----------')
        assert res == expected, f'got {res} while expected {expected}'
        print('pass')