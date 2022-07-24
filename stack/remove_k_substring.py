from typing import List

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack: List[List] = [] # (char, count)

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        res = []
        for c, count in stack:
            res.append(c*count)

        return ''.join(res)


if __name__ == "__main__":
    inputs = [
        ("abcd", 2),
        ("deeedbbcccbdaa", 3),
        ("pbbcggttciiippooaais", 2)
    ]
    outputs = [
        "abcd",
        "aa",
        "ps"
    ]

    sol = Solution()
    for (s,k), expected in zip(inputs, outputs):
        res = sol.removeDuplicates(s,k)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
