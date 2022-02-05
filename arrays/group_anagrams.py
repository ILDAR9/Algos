from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ch = [0] * 26
            for c in s:
                ch[ord(c) - ord('a')] += 1
            res[tuple(ch)].append(s)
        return res.values()


if __name__ == "__main__":
    inputs = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"]
    ]
    outputs = [
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        [[""]],
        [["a"]]
    ]
    sol = Solution()
    for strs, expected in zip(inputs, outputs):
        res = sol.groupAnagrams(strs)
        assert sorted(res) == sorted(expected), f"{res} while expected {expected}"
        print("pass")
