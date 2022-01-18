class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join((t[::-1] for t in s.split()))


if __name__ == '__main__':
    # separated only by a single space
    inputs = [
        "Let's take LeetCode contest",
        "God Ding"
    ]
    outputs = [
        "s'teL ekat edoCteeL tsetnoc",
        "doG gniD"
    ]

    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.reverseWords(s)
        assert res == expected, res