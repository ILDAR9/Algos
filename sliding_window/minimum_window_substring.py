class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ts = dict()
        for c in t:
            ts[c] = ts.get(c, 0) + 1
        res = []
        for i, sh in enumerate(s):
            if sh not in ts:
                continue
            temp = [sh]
            ts_temp = ts.copy()
            ts_temp[sh] -= 1
            if not ts_temp[sh]:
                del ts_temp[sh]
            j = i + 1
            del sh
            while j < len(s) and ts_temp:
                ch = s[j]
                temp.append(ch)
                if ch in ts_temp:
                    ts_temp[ch] -= 1
                    if not ts_temp[ch]:
                        del ts_temp[ch]
                j += 1
            if j == len(s) and ts_temp:
                break
            if not res or len(res) > len(temp):
                res = temp
            i += 1

        return "".join(res)


if __name__ == '__main__':
    # s = "ADOBECODEBANC"
    # t = "ABC"

    s = "a"
    t = "aa"

    # "BANC"
    res = Solution().minWindow(s, t)
    print(f"Res: '{res}'")
