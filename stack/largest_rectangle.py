from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        heights.append(0)
        for i, v in enumerate(heights + [0]):
            # peek
            idx = stack[-1]
            if v >= heights[idx]:
                stack.append(i)
                continue

            while heights[idx] > v:
                stack.pop()
                h = heights[idx]
                idx = stack[-1]
                area = h * (i-idx-1)
                if area > max_area:
                    max_area = area
            stack.append(i)

        return max_area

    def largestRectangleAreaRecurs(self, heights: List[int]) -> int:
        """
        start [...) end
        """
        def area_recursive(start, end):
            if start >= end:
                return 0
            minidx = start
            for i in range(start, end):
                if heights[minidx] > heights[i]:
                    minidx = i
            return max((end-start) * heights[minidx],
                       area_recursive(start, minidx),
                       area_recursive(minidx+1, end))

        return area_recursive(0, len(heights))


if __name__ == "__main__":
    inputs = [
        [2, 1, 5, 6, 2, 3],
        [2, 4]
    ]
    outputs = [
        10,
        4
    ]

    sol = Solution()
    for hist, expected in zip(inputs, outputs):
        res = sol.largestRectangleArea(hist)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
