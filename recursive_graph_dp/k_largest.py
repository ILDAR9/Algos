from typing import List

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l, r):
            # some random number
            pivot = nums[r]
            # key pointer
            p = l
            # except r
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quick_select(l, p-1)
            elif p < k:
                return quick_select(p+1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)




    def findKthLargest_space(self, nums, k):
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



if __name__ == "__main__":
    inputs = [
        ([3,2,1,5,6,4], 2),
        ([3,2,3,1,2,4,5,5,6], 4)
    ]
    outputs = [
        5,
        4
    ]

    sol = Solution()
    for (nums, k), expected in zip(inputs, outputs):
        res = sol.findKthLargest(nums, k)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')