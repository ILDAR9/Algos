class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pass

if __name__ == "__main__":
    inputs = [
        [[1,1],[2,2],[3,3]],
        [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    ]
    outputs = [
        3,
        4
    ]
    sol = Solution()
    for points, expected in zip(inputs, outputs):
        res = sol.maxPoints(points)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")