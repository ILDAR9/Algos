class Solution(object):
    def isNumber(self, s):
        DIGIT = "digit"
        SIGN = "sign"
        DOT = "dot"
        EXPONENT = "exponent"
        dfa = [
            {DIGIT: 1, SIGN: 2, DOT: 3},
            {DIGIT: 1, DOT: 4, EXPONENT: 5},
            {DIGIT: 1, DOT: 3},
            {DIGIT: 4},
            {DIGIT: 4, EXPONENT: 5},
            {SIGN: 6, DIGIT: 7},
            {DIGIT: 7},
            {DIGIT: 7}
        ]
        FINAL_STATES = [1, 4, 7]

        current_state = 0
        for c in s:
            if c.isdigit():
                action = DIGIT
            elif c in ["+", "-"]:
                action = SIGN
            elif c in ["e", "E"]:
                action = EXPONENT
            elif c == ".":
                action = DOT
            else:
                return False

            if action not in dfa[current_state]:
                return False

            current_state = dfa[current_state][action]

        return current_state in FINAL_STATES


if __name__ == "__main__":
    inputs = [
        "0",
        "e",
        "."
    ]
    outputs = [
        True,
        False,
        False
    ]
    sol = Solution()
    for s, expected in zip(inputs, outputs):
        res = sol.isNumber(s)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
