class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
        	temp = one
        	one += two
        	two = temp
        return one

if __name__ == "__main__":
    inputs = [
        2,
        3
    ]
    outputs = [
        2,
        3
    ]
    sol = Solution()
    for n, expected in zip(inputs, outputs):
        res = sol.climbStairs(n)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")