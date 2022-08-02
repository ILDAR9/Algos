class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):

            if part == '.' or not part:
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)


if __name__ == "__main__":
    inputs = [
        "/home/",
        "/../",
        "/home//foo/"
    ]
    outputs = [
        "/home",
        "/",
        "/home/foo"
    ]
    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.simplifyPath(s)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
