from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            prev = res[-1]
            row = [x+y for x,y in zip([0]+prev, prev+[0])]
            res.append(row)
        return res

if __name__ == "__main__":
    inputs = [
        5,
        1
    ]
    outputs = [
        [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]],
        [[1]]
    ]
    sol = Solution()
    for nums, expected in zip(inputs, outputs):
        res = sol.generate(nums)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
