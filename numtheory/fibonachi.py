
class Solution:

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        alpha = 5. ** 0.5
        num = (1. + alpha) / 2
        return round(num ** n / alpha)


    def fib_cache(self, n: int) -> int:
        if n <= 1:
            return n
        cache = [0] * (n+1)
        cache[1] = 1
        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[-1]

    def __init__(self):
        self.mem = {0: 0, 1: 1, 2: 1}

    def fib_rec(self, n: int) -> int:
        if n in self.mem:
            return self.mem[n]
        res = self.fib_rec(n-1) + self.fib_rec(n-2)
        self.mem[n] = res
        return res


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

    for n, expected in zip(inputs, outputs):
        sol = Solution()
        res = sol.fib(n)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
