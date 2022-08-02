from typing import Optional
import sys


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(node, accum):
    if (node == None):
        return
    accum.append(node.data)
    preOrder(node.left, accum)
    preOrder(node.right, accum)


class Solution:

    def findIndex(self, Str: str, si: int, ei: int) -> int:
        """
        function to return the index of 'close' parenthesis
        """
        if (si > ei):
            return -1

        s = []
        for i in range(si, ei + 1):

            # if open parenthesis, push it
            if (Str[i] == '('):
                s.append(Str[i])

            # if close parenthesis
            elif (Str[i] == ')'):
                if (s[-1] == '('):
                    s.pop()

                    # if stack is empty, this is the required index
                    if not s:
                        return i
        # if not found return -1
        return -1

    def treeFromString(self, Str: str, si: int, ei: int) -> Optional[TreeNode]:
        # Base case
        if (si > ei):
            return None

        # new root
        root = TreeNode(ord(Str[si]) - ord('0'))
        index = -1

        # if next char is '(' find the index of its complement ')'
        if (si + 1 <= ei and Str[si + 1] == '('):
            index = self.findIndex(Str, si + 1, ei)

        # if index found
        if (index != -1):

            # call for left subtree
            root.left = self.treeFromString(Str, si + 2, index - 1)

            # call for right subtree
            root.right = self.treeFromString(Str, index + 2, ei - 1)
        return root


if __name__ == "__main__":
    sol = Solution()

    inputs = [
        "1(2)(3)",
        "4(2(3)(1))(6(5))"
    ]
    expected_list = [
        [1, 2, 3],
        [4, 2, 3, 1, 6, 5]
    ]

    sol = Solution()
    for inputstr, expected in zip(inputs, expected_list):
        root = sol.treeFromString(inputstr, 0, len(inputstr) - 1)
        res = []
        preOrder(root, res)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
