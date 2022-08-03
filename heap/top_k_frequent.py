from typing import List
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        negative_counter = defaultdict(lambda : 0)
        for x in nums:
            negative_counter[x] -= 1
        max_heap = [(c,x) for x,c in negative_counter.items()]
        heapq.heapify(max_heap)
        res = []
        for i in range(k):
            _, x = heapq.heappop(max_heap)
            res.append(x)

        return res



if __name__ == "__main__":
    inputs = [
        ([1,1,1,2,2,3], 2),
        ([1], 1)
    ]
    outputs = [
        [1,2],
        [1]
    ]
    sol = Solution()
    for (points, k), expected in zip(inputs, outputs):
        res = sol.topKFrequent(points, k)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
