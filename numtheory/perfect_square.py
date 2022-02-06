class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return 1

        def binsearch(left, right):
            if left > right:
                return False
            mid = (left + right) // 2
            v = mid * mid
            if v == num:
                return True

            if v < num:
                return binsearch(mid + 1, right)
            else:
                return binsearch(left, mid-1)

        return binsearch(2, num // 2)


if __name__ == "__main__":
    inputs = [
        16,
        14,
        1
    ]
    outputs = [
        True,
        False,
        True
    ]

    sol = Solution()
    for n, expected in zip(inputs, outputs):
        res = sol.isPerfectSquare(n)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
