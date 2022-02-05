from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for x in range(1, n + 1):
            res[x] = res[x & (x-1)] + 1
        return res


if __name__ == "__main__":
    inputs = [
        2,
        5
    ]
    outputs = [
        [0, 1, 1],
        [0, 1, 1, 2, 1, 2]
    ]
    sol = Solution()
    for n, expected in zip(inputs, outputs):
        res = sol.countBits(n)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
