from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLUMNS = len(board[0])

        path = set()
        def backtrack(r,c,i) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or \
                c < 0 or c >= COLUMNS or \
                board[r][c] != word[i] or (r,c) in path:
                return False
            point = (r, c)
            path.add(point)
            res = backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1) or \
                  backtrack(r,c-1,i+1) or backtrack(r,c+1,i+1)

            path.remove(point)
            return res

        for r in range(ROWS):
            for c in range(COLUMNS):
                path = set()
                if backtrack(r, c, 0):
                    return True

        return False


if __name__ == "__main__":
    inputs = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    ]
    outputs = [
        True,
        True,
        True,
        False
    ]

    sol = Solution()
    for (board, word), expected in zip(inputs, outputs):
        res = sol.exist(board, word)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')