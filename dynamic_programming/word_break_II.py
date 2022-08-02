
from typing import List

class Solution:

    def wordBreakCount(self, in_str: str, word_list: List[str]) -> List[str]:
        dp = dict()
        word_set = set(word_list)

        def dfs(s):
            if s == '':
                return 1
            if s in dp:
                return dp[s]

            cur_count = 0
            for end in range(1, len(s) + 1):
                if s[:end] in word_set:
                    cur_count += dfs(s[end:])
                        

            dp[s] = cur_count
            return dp[s]


        res = dfs(in_str)
        return res

    def wordBreakAll(self, in_str: str, word_list: List[str]) -> List[str]:
        dp = dict()
        word_set = set(word_list)

        def dfs(s):
            if s == '':
                return [[]]
            if s in dp:
                return dp[s]

            cur_words = []
            for end in range(1, len(s) + 1):
                if s[:end] in word_set:
                    for rest in dfs(s[end:]):
                        cur_words.append([s[:end]] + rest)

            dp[s] = cur_words
            return dp[s]


        res = [' '.join(words) for words in dfs(in_str)]
        return res

if __name__ == '__main__':
    # separated only by a single space
    inputs = [
        ("catsanddog", ["cat","cats","and","sand","dog"]),
        ("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]),
        ("catsandog", ["cats","dog","sand","and","cat"])
    ]
    outputs = [
        ["cats and dog","cat sand dog"],
        ["pine apple pen apple","pineapple pen apple","pine applepen apple"],
        []
    ]

    sol = Solution()
    for (s, d), expected in zip(inputs, outputs):
        res = sol.wordBreakCount(s, d)
        assert res == len(expected), res
        print('pass')