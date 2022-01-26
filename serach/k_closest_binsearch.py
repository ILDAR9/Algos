from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        if n <= k:
            return points
        distances = list(map(self.distance, points))
        indices = list(range(n))
        found = []
        leftdist, rightdist = 0, max(distances)
        while k:
            mid = leftdist + (rightdist - leftdist) / 2
            leftlist, rightlist = self.split_points(indices, distances, mid)
            if len(leftlist) > k:
                indices = leftlist
                rightdist = mid
            else:
                indices = rightlist
                found += leftlist
                k -= len(leftlist)
                leftdist = mid
        return list(map(points.__getitem__, found))

    def split_points(self, indices: List[int], distances: List[float], mid_dist: float):
        leftlist = []
        rightlist = []
        for i in indices:
            if distances[i] < mid_dist:
                leftlist.append(i)
            else:
                rightlist.append(i)
        return leftlist, rightlist

    def distance(self, points):
        return points[0]**2 + points[1]**2


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
