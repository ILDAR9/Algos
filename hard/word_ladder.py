from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(set)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + '*' + word[i+1:]
                adj[pat].add(word)

        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            q_len = len(q)
            for _ in range(q_len):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pat = word[:i] + '*' + word[i+1:]
                    for word_neig in adj[pat]:
                        if word_neig not in visited:
                            q.append(word_neig)
                            visited.add(word_neig)

            
            res += 1

        return 0



if __name__ == "__main__":
    inputs = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"]),
        ("hit", "cog", ["hot","dot","dog","lot","log"])
    ]
    outputs = [
        5,
        0
    ]

    sol = Solution()
    for (begin, end, word_list), expected in zip(inputs, outputs):
        res = sol.ladderLength(begin, end, word_list)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')

