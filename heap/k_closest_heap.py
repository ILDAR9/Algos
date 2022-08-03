from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points

        min_heap = []

        # fillup the min heap
        for x, y in points:
            dist = x**2 + y**2
            min_heap.append((dist, x, y))

        res = []
        heapq.heapify(min_heap)
        for i in range(k):
            _, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        return res


if __name__ == "__main__":
    inputs = [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
    ]
    outputs = [
        [[-2, 2]],
        [[3, 3], [-2, 4]]
    ]
    sol = Solution()
    for (points, k), expected in zip(inputs, outputs):
        res = sol.kClosest(points, k)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
