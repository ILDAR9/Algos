class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if not s[left].isalpha() and not s[left].isdigit():
                left += 1
                continue
            if not s[right].isalpha() and not s[right].isdigit():
                right -= 1
                continue
            x = s[left].lower() if s[left].isupper() else s[left]
            y = s[right].lower() if s[right].isupper() else s[right]
            if x != y:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    inputs = [
        "0P",
        "A man, a plan, a canal: Panama",
        "race a car",
        " "
    ]
    outputs = [
        False,
        True,
        False,
        True
    ]
    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.isPalindrome(s)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
