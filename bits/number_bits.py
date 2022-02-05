class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n != 0:
            n &= (n-1)
        return sum

if __name__ == "__main__":
    inputs = [
        "00000000000000000000000000001011",
        "00000000000000000000000010000000",
        "11111111111111111111111111111101"
    ]
    outputs = [
        1,
        1,
        31
    ]
    sol = Solution()
    for n, expected in zip(inputs, outputs):
        n = int(n, 2)
        res = sol.hammingWeight(n)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
