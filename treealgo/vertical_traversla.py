from typing import Optional, List, Dict
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        grx: Dict[List[val]] = defaultdict(list)

        def dfs(node, x, y):
            grx[x].append((y, node.val))
            if node.left: dfs(node.left, x-1, y+1)
            if node.right: dfs(node.right, x+1, y+1)

        dfs(root, 0, 0)

        return [[v[1] for v in sorted(grx[x])] for x in sorted(grx.keys())]

        

if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [3,1,4,0,2,2],
        [3,9,20,None,None,15,7],
        [1,2,3,4,5,6,7],
        [1,2,3,4,6,5,7]

    ]
    expected_list = [
        [[0],[1],[3,2,2],[4]],
        [[9],[3,15],[20],[7]],
        [[4],[2],[1,5,6],[3],[7]],
        [[4],[2],[1,5,6],[3],[7]]
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

        res = sol.verticalTraversal(root)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')