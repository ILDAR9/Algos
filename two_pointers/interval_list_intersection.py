from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # your code here
        res = []
        ui = 0
        for t in A:
            if ui >= len(B):
                break

            # Main logic here
            begin = t[0]
            end = t[1]

            while ui < len(B):
                t2 = B[ui]
                if end < t2[0]:
                    break

                intersect = self.find_intersection(t, t2)
                if intersect is not None:
                    res.append(intersect)

                if end >= t2[1]:
                    ui += 1
                else:
                    break
        return res

    @staticmethod
    def find_intersection(a, b) -> List[int]:
        interval = [max(a[0], b[0]), min(a[1], b[1])]
        size = interval[1] - interval[0]
        return interval if size >= 0 else None


if __name__ == '__main__':
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = Solution().intervalIntersection(A, B)
    print(res)
