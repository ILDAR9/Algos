class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        for i in range(n):
        	# odd case
        	l, r = i, i
        	while l >= 0 and r < n and s[l] == s[r]:
        		if (r - l + 1) > len(res):
        			res = s[l: r+1]
        		l -= 1
        		r += 1

        	# eeven case
        	l, r = i, i + 1
        	while l >= 0 and r < n and s[l] == s[r]:
        		if (r - l + 1) > len(res):
        			res = s[l: r+1]
        		l -= 1
        		r += 1

        return res


if __name__ == "__main__":
    inputs = [
        "babad",
        "cbbd"
    ]
    outputs = [
        "bad",
        "bb"
    ]

    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.longestPalindrome(s)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')