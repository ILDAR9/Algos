from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    	if not root:
    		return TreeNode(val)
        
    	def insert(node, val) -> None:

    		if val > node.val:
    			if node.right:
    				insert(node.right, val)
    			else:
    				node.right = TreeNode(val)
    		else:
    			if node.left:
    				insert(node.left, val)
    			else:
    				node.left = TreeNode(val)

    	insert(root, val)
    	return root


if __name__ == "__main__":
    sol = Solution()

    inputs = [
        ([4,2,7,1,3], 5),
        ([40,20,60,10,30,50,70], 25),
        ([4,2,7,1,3,None,None,None,None,None,None], 5)
    ]
    expected_list = [
        [4,2,7,1,3,5],
        [40,20,60,10,30,50,70,None,None,25],
        [4,2,7,1,3,5]
    ]


    for (input_list, val), expected in zip(inputs, expected_list):
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
        res = sol.insertIntoBST(root, val)
        print()
        print(root)
        print('----------')
        assert res == expected, f'got {res} while expected {expected}'
        print('pass')