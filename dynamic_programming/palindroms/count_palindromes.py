class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            l, r = i, i+ 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

if __name__ == "__main__":
    inputs = [
        "abc",
        "aaa"
    ]
    outputs = [
        3,
        6
    ]

    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.countSubstrings(s)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')