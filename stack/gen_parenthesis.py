from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        stack: List[str] = []

        def backtrack(open_n: int, close_n: int):
            if open_n == close_n == n:
                res.append(''.join(stack))
                return

            if open_n < n:
                stack.append('(')
                backtrack(open_n+1, close_n)
                stack.pop()

            if close_n < open_n:
                stack.append(')')
                backtrack(open_n, close_n+1)
                stack.pop()

        backtrack(0, 0)

        return res


if __name__ == "__main__":
    inputs = [
        3,
        1
    ]
    outputs = [
        ["((()))","(()())","(())()","()(())","()()()"],
        ["()"]
    ]

    sol = Solution()
    for n, expected in zip(inputs, outputs):
        res = sol.generateParenthesis(n)
        assert sorted(res) == sorted(expected), f"{res} while expected {expected}"
        print('pass')
