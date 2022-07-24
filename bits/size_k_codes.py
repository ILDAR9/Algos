class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        code_set = set()

        for i in range(len(s) - k + 1):
            code_set.add(s[i:i+k])

        return len(code_set) == 2 ** k

if __name__ == "__main__":
    inputs = [
        ("00110110", 2),
        ("0110", 1),
        ("0110", 2)
    ]
    outputs = [
        True,
        True,
        False
    ]
    sol = Solution()
    for (s, k), expected in zip(inputs, outputs):
        res = sol.hasAllCodes(s, k)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
