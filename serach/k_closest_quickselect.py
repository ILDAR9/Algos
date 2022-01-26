from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points
        self.quick_select(points, k)
        return points[:k]

    def quick_select(self, points, k) -> None:
        pivot_idx = len(points)
        left, right = 0, len(points)-1
        while pivot_idx != k:
            pivot_idx = self.partition(points, left, right)
            if pivot_idx < k:
                left = pivot_idx
            else:
                right = pivot_idx-1

    def choose_pivot_index(self, left, right) -> int:
        return left + (right - left) // 2

    def partition(self, points, left, right) -> None:
        pivot_index = self.choose_pivot_index(left, right)
        pivot_dist = self.distance(points[pivot_index])
        while left < right:
            if self.distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        if self.distance(points[left]) < pivot_dist:
            left += 1

        return left

    def distance(self, points) -> int:
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
