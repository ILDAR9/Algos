class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        prev_2 = 0
        prev_1 = 1
        for i in range(2, n+1):
            temp = prev_1
            prev_1 += prev_2
            prev_2 = temp

        return prev_1



if __name__ == "__main__":
    inputs = [
        2,
        3,
        4
    ]
    outputs = [
        1,
        2,
        3
    ]
    sol = Solution()
    for n, expected in zip(inputs, outputs):
        res = sol.fib(n)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")