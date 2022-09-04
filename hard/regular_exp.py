from typing import Tuple, Set

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top down memorisation

        cash: Dict[Tuple] = dict()
        STAR = '*'
        POINT = '.'
        def dfs(i: int, j: int):
        	if (i, j) in cash:
        		return cash[(i, j)]
        	if i >= len(s) and j >= len(p):
        		return True
        	if j >= len(p):
        		return False

        	match: bool = i < len(s) and (s[i] == p[j] or p[j] == POINT)
        	# hadle asterics
        	if j+1 < len(p) and p[j+1] == STAR:
        		res = dfs(i, j+2) or (match and dfs(i+1, j))
        		cash[(i, j)] = res
        		return res
        	if match:
        		res = dfs(i+1, j+1)
        		cash[(i, j)] = res
        		return res
        	cash[(i, j)] = False
        	return False
        return dfs(0, 0)



if __name__ == "__main__":
    inputs = [
        ("aa", "a"),
        ("aa", "a*"),
        ("ab", ".*")
    ]
    outputs = [
        False,
        True,
        True
    ]

    sol = Solution()
    for (s, p), expected in zip(inputs, outputs):
        res = sol.isMatch(s, p)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')


"""
scopre:
1. It is guaranteed for each appearance of the character '*',
   there will be a previous valid character to match.
"""