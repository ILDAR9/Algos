class Solution(object):
    def strStr(self, haystack, needle):
        nl, ml = len(needle), len(haystack)
        if nl == 0:
            return nl
        if ml < nl:
            return -1
        for i in range(ml - nl + 1):
            if haystack[i:i+nl] == needle:
                return i
        return -1


if __name__ == "__main__":
    inputs = [
        ("mississippi", "issip"),
        ("hello", "ll"),
        ("hello", "lo"),
        ("hello", "o"),
        ("aaaaa", "bba"),
        ("", "")
    ]
    outputs = [
        4,
        2,
        3,
        4,
        -1,
        0
    ]

    sol = Solution()
    for (s1,s2), expected in zip(inputs, outputs):
        res = sol.strStr(s1,s2)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
