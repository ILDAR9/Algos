from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        preword = words[0]
        for word in words[1:]:
            i = 0
            for c1, c2 in zip(preword, word):
                if order.index(c1) < order.index(c2):
                    break
                if order.index(c1) == order.index(c2):
                    i+=1
                    continue
                return False
            if len(preword) > len(word) and i == len(word):
                return False
            preword = word

        return True


if __name__ == "__main__":
    inputs = [
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"),
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz")
    ]
    expected_list = [
        True,
        False,
        False
    ]
    sol = Solution()
    for (words, order), expected in zip(inputs, expected_list):
        output = sol.isAlienSorted(words, order)
        assert output == expected, f'{output} while expected {expected} for words {words}'
        print("pass")
