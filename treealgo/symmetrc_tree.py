class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"v={self.val} l={self.left} r={self.right}"


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.ismirror(root, root)

    def ismirror(self, t1: TreeNode, t2: TreeNode):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and self.ismirror(t1.left, t2.right) and self.ismirror(t1.right, t2.left)


if __name__ == '__main__':
    val_list = [1, 2, 2, 3, 4, 4, 3]
    # val_list = [1, 2, 2, None, 3, None, 3]
    trenode_list = list(map(TreeNode, val_list))
    count = len(val_list)
    for i, node in enumerate(trenode_list):
        left_idx = i * 2 + 1
        if left_idx < count: node.left = trenode_list[left_idx]
        right_idx = i * 2 + 2
        if left_idx < count: node.right = trenode_list[right_idx]

    # print(trenode_list[0])
    res = Solution().isSymmetric(trenode_list[0])
    print("Res", res)
