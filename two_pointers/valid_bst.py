import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"v={self.val} l={self.left} r={self.right}"


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                    validate(node.left, low, node.val))

        return validate(root)


if __name__ == '__main__':
    val_list = [2, 1, 3]
    # val_list = [5, 1, 4, None, None, 3, 6]
    trenode_list = list(map(TreeNode, val_list))
    count = len(val_list)
    for i, node in enumerate(trenode_list):
        left_idx = i * 2 + 1
        if left_idx < count: node.left = trenode_list[left_idx]
        right_idx = i * 2 + 2
        if left_idx < count: node.right = trenode_list[right_idx]

    # print(trenode_list[0])
    res = Solution().isValidBST(trenode_list[0])
    print("Res", res)
