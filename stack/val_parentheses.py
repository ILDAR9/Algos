class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        idx_remove = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                idx_remove.append(i)
            else:
                stack.pop()
        idx_remove += stack
        res = []
        for i, c in enumerate(s):
            if i in idx_remove:
                continue
            res.append(c)
        return "".join(res)


if __name__ == "__main__":
    inputs = [
        "lee(t(c)o)de)",
        "a)b(c)d",
        "))(("
    ]
    outputs = [
        "lee(t(c)o)de",
        "ab(c)d",
        ""
    ]

    sol = Solution()
    for hist, expected in zip(inputs, outputs):
        res = sol.minRemoveToMakeValid(hist)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
