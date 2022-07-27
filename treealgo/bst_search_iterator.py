# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        stack = []
        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left
        self.stack = stack
        

    def next(self) -> int:
        cur = self.stack.pop()
        child = cur.right
        while child:
            self.stack.append(child)
            child = child.left

        return cur.val
        

    def hasNext(self) -> bool:
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()