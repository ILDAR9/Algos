from collections import Counter, defaultdict
from typing import Tuple

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        res: Tuple[int] = (0, 0)
        res_len = float('infinity')

        count_T = dict(Counter(t))
        window_S = defaultdict(lambda : 0)

        need = len(count_T)
        have = 0

        l = 0

        # update right pointer
        for r, c in enumerate(s):
            window_S[c] += 1
            if c in count_T and window_S[c] == count_T[c]:
                have += 1

            # find local shortes by changing left pointer
            while have == need:
                cur_len = r-l+1
                if cur_len < res_len:
                    # update result
                    res = (l, r)
                    res_len = cur_len
                # shrink out window from left by one char
                left_c = s[l]
                window_S[left_c] -= 1
                if left_c in count_T and window_S[left_c] < count_T[left_c]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float('infinity') else ''


if __name__ == "__main__":
    inputs = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa")
    ]
    outputs = [
        "BANC",
        "a",
        ""
    ]

    sol = Solution()
    for (s, t), expected in zip(inputs, outputs):
        res = sol.minWindow(s, t)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')

