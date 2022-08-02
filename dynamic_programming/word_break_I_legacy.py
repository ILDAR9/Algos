from typing import List

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        len_s = len(s)
        dp = [True] + [False] * (len_s)
        word_set = set(wordDict)

        for end in range(1, len_s + 1):
            for start in range(end):
                if dp[start] and s[start:end] in word_set:
                    dp[end] = True
                    break
        
        return dp[len_s]

    def wordBreakBFS(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False

    def wordBreakDFS(self, s: str, wordDict: List[str]) -> bool:
        start = 0
        stack = [start]
        cash = set()
        d = set(wordDict)
        len_s = len(s)
        
        while True:
            start = stack.pop()
            if start == len_s:
                return True
            for end in range(start + 1, len(s)+ 1):
                if end in cash:
                    continue
                if s[start:end] in d:
                    stack.append(end)
            if not stack:
                break
            cash.add(start)
        
        return False



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