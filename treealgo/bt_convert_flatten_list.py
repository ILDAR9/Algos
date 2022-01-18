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
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            else:
                pass
            node = node.right

    def flatten_stack(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        START = 0
        END = 1
        stack = [(root, START)]
        tail_node = None
        while stack:
            node, state = stack.pop()
            if not node.left and not node.right:
                tail_node = node
                continue

            if state == START:
                if node.left:
                    stack.append((node, END))
                    stack.append((node.left, START))
                elif node.right:
                    stack.append((node.right, START))
            else:

                right_node = node.right
                if tail_node:
                    tail_node.right = right_node
                    node.right = node.left
                    node.left = None
                # avoid none elements in the stack
                if right_node:
                    stack.append((right_node, START))

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