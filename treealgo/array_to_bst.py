from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def helper(l, r) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l+r) // 2
            node = TreeNode(nums[mid])
            node.left = helper(l, mid-1)
            node.right = helper(mid+1, r)
            return node


        return helper(0, len(nums) - 1)

if __name__ == "__main__":
    sol = Solution()

    inputs = [
        [-10,-3,0,5,9],
        [1,3]

    ]
    expected_list = [
        [0,-3,9,-10,None,5],
        [3,1],

    ]


    for input_list, expected in zip(inputs, expected_list):
        sol = Solution()
        res = sol.sortedArrayToBST(input_list)
        # print()
        # print(root)
        # print('----------')
        assert res == expected, f'got {res} while expected {expected}'
        print('pass')