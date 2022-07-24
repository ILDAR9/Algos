# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        # return str(self.val)
        return f"[{self.val} ({self.next}) l={self.left}]"

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        cur, leftmost_child = root, root.left
        while leftmost_child:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next
            if not cur:
                cur = leftmost_child
                leftmost_child = cur.left

        return root

if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [1,2,3,4,5,6,7]
    ]
    expected_list = [
        [1,None,2,3,None,4,5,6,7,None]
    ]


    for input_list, expected in zip(inputs, expected_list):
        if not input_list:
            root = None
        else:
            root = Node(input_list[0])
            nodes = [root]
            for i, v in enumerate(input_list[1:], start = 1):
                node = Node(v)
                parent_node = nodes[(i-1) // 2]
                if i % 2 == 1:
                    parent_node.left = node
                else:
                    parent_node.right = node
                nodes.append(node)

        sol = Solution()
        res = sol.connect(root)
        # assert res == expected, res
        print()
        print(root)
        print('----------')