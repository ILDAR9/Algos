from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        stack = []
        first, last = None, None
        cur = root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                if last:
                    last.right = cur
                    cur.left = last
                else:
                    first = cur
                last = cur

                cur = cur.right
            else:
                break
            
        first.left = last
        last.right = first
        return first

    def treeToDoublyListRecursion(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(node: 'Optional[Node]') -> None:
            if not node:
                return

            nonlocal first, last

            dfs(node.left)

            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node

            dfs(node.right)

        if not root:
            return
        first, last = None, None
        dfs(root)
        first.left = last
        last.right = first
        return first


if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [4, 2, 5, 1, 3]
    ]
    expected_list = [
        [1, 2, 3, 4, 5]
    ]

    for input_list, expected in zip(inputs, expected_list):
        if not input_list:
            root = None
        else:
            root = Node(input_list[0])
            nodes = [root]
            for i, v in enumerate(input_list[1:], start=1):
                node = Node(v)
                parent_node = nodes[(i-1) // 2]
                if i % 2 == 1:
                    parent_node.left = node
                else:
                    parent_node.right = node
                nodes.append(node)

        print(input_list)
        sol = Solution()
        head = sol.treeToDoublyList(root)
        # assert res == expected, res
        print()
        res = []
        head.left.right = None
        node = head
        while node:
            res.append(node.val)
            node = node.right
            
        print(res)
