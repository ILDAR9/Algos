from typing import List

class Solution:
    def moveZeroes(self, ar: List[int]) -> None:
        last_idx = 0
        ZERO = 0
        for i, c in enumerate(ar):
            if c != ZERO:
                ar[last_idx] = c
                last_idx += 1

        in_arr[last_idx:] = [ZERO] * (len(ar) - last_idx)


if __name__ == "__main__":
    # in_arr =    [1, 10, 20, 0, 59, 63,  0, 88,  0]
    in_arr = [0,1,0,3,12]
    sol = Solution()
    sol.moveZeroes(in_arr)
    print(in_arr)