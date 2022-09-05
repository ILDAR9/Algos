class Solution:
    def calculate(self, s: str) -> int:
        pass


if __name__ == "__main__":
    inputs = [
        "1 + 1",
        " 2-1 + 2 ",
        "(1+(4+5+2)-3)+(6+8)"
    ]
    outputs = [
        2,
        3,
        23
    ]

    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.calculate(s)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')