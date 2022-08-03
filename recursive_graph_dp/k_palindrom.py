from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        counter = Counter(s)
        count_odd = sum(1 for c in counter.values() if c % 2 == 1)
        return count_odd <= k



if __name__ == "__main__":
    inputs = [
        ("annabelle", 2),
        ("leetcode", 3),
        ("true", 4)
    ]
    outputs = [
        True,
        False,
        True
    ]
    sol = Solution()
    for (amount, coins), expected in zip(inputs, outputs):
        res = sol.canConstruct(amount, coins)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")