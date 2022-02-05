class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n != 0:
            res += (n & 1) << power
            n >>= 1
            power -= 1
        return res       


if __name__ == "__main__":
    inputs = [
        "00000010100101000001111010011100",
        "11111111111111111111111111111101"
    ]
    outputs = [
        964176192,
        3221225471
    ]
    sol = Solution()
    for n, expected in zip(inputs, outputs):
        n = int(n, 2)
        res = sol.reverseBits(n)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
