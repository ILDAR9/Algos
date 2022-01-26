
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, o):
        return self.val == o.val if o else None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            mark_cur = node == p or node == q
            mark_left = dfs(node.left) if node.left else False
            mark_right = dfs(node.right) if node.right else False
            if mark_cur + mark_left + mark_right >= 2:
                nonlocal ancestor
                ancestor = node
                return False
            return any([mark_cur, mark_left, mark_right])

        ancestor = root
        dfs(root)
        return ancestor


if __name__ == "__main__":
    sol = Solution()

    inputs = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],  5,  1),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],  5, 4),
        ([1, 2], 1, 2)
    ]
    expected_list = [
        3,
        5,
        1
    ]

    sol = Solution()
    for (input_list, p, q), expected in zip(inputs, expected_list):
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

        p = TreeNode(p)
        q = TreeNode(q)
        res = sol.lowestCommonAncestor(root, p, q)
        assert res.val == expected, f"{res.val} while expected {expected}"
        print('pass')
