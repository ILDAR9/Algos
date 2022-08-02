from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """double backtrack"""
        counter = dict(Counter(nums))
        result = []
        perm = []

        def backtrack():
        	if len(perm) == len(nums):
        		result.append(perm[:])

        	for c in counter.keys():
        		if counter[c]:
        			counter[c] -= 1
        			perm.append(c)


        			backtrack()

        			counter[c] += 1
        			perm.pop()

        backtrack()
        return result

if __name__ == "__main__":
    inputs = [
        [1,1,2],
        [1,2,3]
    ]
    outputs = [
        [[1,1,2],
 		[1,2,1],
 		[2,1,1]  ],
 		[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.permuteUnique(nums)
        assert sorted(res) == sorted(expected), f"{res} while expected {expected}"
        print("pass")