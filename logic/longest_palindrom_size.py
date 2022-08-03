from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        length = sum(x if x%2==0 else x-1 for x in counter.values())
        if any(x % 2 == 1 for x in counter.values()):
            length += 1
        return length

if __name__ == "__main__":
    inputs = [
        "abccccdd",
        "a"
    ]
    outputs = [
        7,
        1
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.longestPalindrome(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
