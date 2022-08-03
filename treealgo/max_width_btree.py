from typing import Optional, Tuple
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if not self.left and not self.right:
            return str(self.val)
        return f"{self.val} ({self.left} {self.right})"

TYPE_NODE = Tuple[TreeNode, int]

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # node, index
        queue: List[TYPE_NODE] = deque([(root, 1)])
        max_width = 0
        while queue:
            # get top width
            _, left_idx = queue[0]
            _, right_idx = queue[-1]
            width = right_idx - left_idx + 1
            max_width = max(max_width, width)

            # exploration
            new_q: List[TYPE_NODE] = deque()
            while queue:
                node, idx= queue.popleft()
                if node.left:
                    new_q.append((node.left, idx*2))
                if node.right:
                    new_q.append((node.right, idx*2+1))
            queue = new_q
        return max_width




if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [1,3,2,5,3,None,9],
        [1,3,2,5,None,None,9,6,None,7],
        [1,3,2,5]
    ]
    expected_list = [
        4,
        7,
        2
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
        res = sol.widthOfBinaryTree(root)
        print()
        print(root)
        print('----------')
        assert res == expected, f'got {res} while expected {expected}'
        print('pass')