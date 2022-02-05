class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)
        
        # abs(a) >= abs(b) --> 
        # a determines the sign
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow
        
        return x * sign


if __name__ == "__main__":
    inputs = [
        (1, 2),
        (2, 3),
        (0, 0),
        (0, 1),
        (-2, -3)
    ]
    outputs = [
        3,
        5,
        0,
        1,
        -5
    ]
    sol = Solution()
    for (a, b), expected in zip(inputs, outputs):
        res = sol.getSum(a, b)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
