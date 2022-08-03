from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        if rowIndex == 0:
            return prev
        for i in range(1, rowIndex+1):
            row = [x+y for x,y in zip([0] + prev, prev + [0])]
            prev = row
        return prev

if __name__ == "__main__":
    inputs = [
        3,
        0,
        1
    ]
    outputs = [
        [1,3,3,1],
        [1],
        [1,1]
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.getRow(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
