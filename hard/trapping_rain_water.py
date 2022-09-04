from typing import List
import heapq


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
        	return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[0], height[r]
        res = 0
        while (l<r):
        	if left_max <= right_max:
        		l+=1
        		left_max = max(left_max, height[l])
        		res += left_max - height[l]
        	else:
        		r-=1
        		right_max = max(right_max, height[r])
        		res += right_max - height[r]
        return res


if __name__ == "__main__":
    inputs = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5]
    ]
    outputs = [
        6,
        9
    ]

    sol = Solution()
    for heights, expected in zip(inputs, outputs):
        res = sol.trap(heights)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')

"""
heapq


"""