class Solution:
    def findKthLargest(self, nums, k):
        pivot = nums[len(nums) // 2]
        left = [l for l in nums if l < pivot]
        equal = [e for e in nums if e == pivot]
        right = [r for r in nums if r > pivot]

        if k <= len(right):
            return self.findKthLargest(right, k)
        elif (k - len(right)) <= len(equal):
            return equal[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(equal))


if __name__ == '__main__':
    # nums = [3, 2, 1, 5, 6, 4]
    # k = 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4

    res = Solution().findKthLargest(nums, k)
    print("Res", res)  # 5
