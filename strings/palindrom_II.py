class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self._is_palindrom(s[l+1: r+1]) or self._is_palindrom(s[l: r])
            l+=1
            r-=1

        return True


    def _is_palindrom(self, s: str) -> bool:
        for i in range(len(s)  // 2):
            if s[i] != s[-i-1]:
                return False
        return True

if __name__ == "__main__":
    inputs = [
        "aba",
        "abca",
        "abc"
    ]
    outputs = [
        True,
        True,
        False
    ]

    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.validPalindrome(s)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')
