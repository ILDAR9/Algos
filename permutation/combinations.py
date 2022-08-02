from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return

            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1)
                comb.pop()

        backtrack(1)
        return res



if __name__ == "__main__":
    inputs = [
        (4, 2),
        (1, 1)
    ]
    outputs = [
        [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ],
        [[1]]
    ]
    sol = Solution()
    for (n, k), expected in zip(inputs, outputs):
        res = sol.combine(n, k)
        assert sorted(res) == sorted(expected), f"{res} while expected {expected}"
        print("pass")