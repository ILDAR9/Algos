from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"v={self.val} l={self.left} r={self.right}"


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res: List[int] = [root.val]
        queue: List[TreeNode] = deque([root.left, root.right])

        while queue:
            q_len = len(queue)

            right_node = None
            for _ in range(q_len):
                node = queue.popleft()
                if not node:
                    continue
                right_node = node
                queue.append(node.left)
                queue.append(node.right)

            if right_node:
                res.append(right_node.val)

        return res



if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [1,2,3,None,5,None,4],
        [1,None,3],
        []
    ]
    expected_list = [
        [1,3,4],
        [1,3],
        []
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

        res = sol.rightSideView(root)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')