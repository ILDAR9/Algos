from collections import deque

class Solution:

    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        
        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1
            
        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))
        
        return ' '.join(d)

    def reverseWordsBasic(self, s: str) -> str:
        return " ".join(s.split()[::-1])


if __name__ == '__main__':
    # separated only by a single space
    inputs = [
        "the sky is blue",
        "  hello world  ",
        "a good   example"
    ]
    outputs = [
        "blue is sky the",
        "world hello",
        "example good a"
    ]

    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.reverseWords(s)
        assert res == expected, res