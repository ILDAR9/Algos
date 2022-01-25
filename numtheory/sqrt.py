class Solution:

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left = self.mySqrt(x>>2) << 1
        right = left + 1
        return left if right * right > x else right

    def mySqrtBinarySearch(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot

        return right


if __name__ == "__main__":
    inputs = [
        36,
        0,
        1,
        4,
        8,
        73
    ]
    outputs = [
        6,
        0,
        1,
        2,
        2,
        8
    ]

    for n, expected in zip(inputs, outputs):
        sol = Solution()
        res = sol.mySqrt(n)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
