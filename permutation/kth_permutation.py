class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        pass

if __name__ == "__main__":
    inputs = [
        (3, 3),
        (4, 9),
        (3, 1)
    ]
    outputs = [
        "213",
        "2314",
        "123"
    ]

    sol = Solution()
    for (n, k), expected in zip(inputs, outputs):
        res = sol.getPermutation(n, k)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')