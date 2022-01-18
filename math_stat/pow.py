class Solution:

    def myPow(self, x, n):
        if n < 0:
            x = 1./x
            n = -n
        
        ans = 1.
        cur = x

        while n > 0:
            if n % 2:
                ans *= cur
            cur **= 2

            n //= 2

        return ans

    def recPow(self, x, n):
        if n == 0:
            return 1.
        
        half = self.recPow(x, n//2)
        if n % 2 == 1:
            return half * half * x
        else:
            return half * half

    def myPowUseRecurs(self, x: float, n: int) -> float:
        if n < 0:
            x = 1. / x
            n = -n
        
        return self.recPow(x, n)

def isclose(a, b, rel_tol=1, abs_tol=1e-04):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

if __name__ == "__main__":
    inputs = [
        (2.00000, 10),
        (2.00000, 3),
        (2.10000, 3),
        (2.00000, -2),
        (0.4, 0),
        (2, 5),
        (8.84372, -5)
    ]
    outputs = [
        1024.00000,
        8,
        9.26100,
        0.25000,
        1.,
        32,
        2e-05
    ]
    sol = Solution()
    for (x, n), expected in zip(inputs, outputs):
        res = sol.myPow(x, n)
        assert isclose(res, expected), f"{res} while expected {expected}"
# 