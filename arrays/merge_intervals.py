from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key = lambda x : x[0])
        left_cur, right_cur = intervals[0]
        for left_x, right_x in intervals[1:]:
            if right_cur < left_x:
                res.append([left_cur, right_cur])
                left_cur = left_x
                right_cur = right_x
            else:
                right_cur = max(right_cur, right_x)
            
        res.append([left_cur, right_cur])

        return res

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]

    # intervals = [[1,4],[4,5]]
    # expected = [[1,5]]

    sol = Solution()
    res = sol.merge(intervals)
    assert res == expected, res