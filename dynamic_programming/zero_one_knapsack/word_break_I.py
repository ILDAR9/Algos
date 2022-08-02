from typing import List

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    	dp = [False] * (len(s) + 1)
    	dp[len(s)] = True

    	for i in range(len(s), -1, -1):

    		for w in wordDict:
    			if i + len(w) <= len(s) and s[i: i+len(w)] == w:
    				dp[i] = dp[i+len(w)]
    			if dp[i]:
    				break

    	return dp[0]


if __name__ == '__main__':
    # separated only by a single space
    inputs = [
        ("leetcode", ["leet","code"]),
        ("applepenapple", ["apple","pen"]),
        ("catsandog", ["cats","dog","sand","and","cat"])
    ]
    outputs = [
        True,
        True,
        False
    ]

    sol = Solution()
    for (s, d), expected in zip(inputs, outputs):
        res = sol.wordBreak(s, d)
        assert res == expected, res
        print('pass')