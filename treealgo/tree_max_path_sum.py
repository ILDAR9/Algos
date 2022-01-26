from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node) -> int:
            
            if not node:
                return 0
            
            leftsum = dfs(node.left)
            rightsum = dfs(node.right)

            curmaxsum =  node.val + max(leftsum, rightsum, leftsum + rightsum, 0)
            nonlocal maxsum
            if maxsum < curmaxsum:
                maxsum = curmaxsum
            return node.val + max(leftsum, rightsum, 0)

        maxsum = root.val
        dfs(root)
        return maxsum


if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [1,-2,3],
        [-3],
        [1, 2, 3],
        [-10, 9, 20, None, None, 15, 7]
    ]
    expected_list = [
        4,
        -3,
        6,
        42
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

        res = sol.maxPathSum(root)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
