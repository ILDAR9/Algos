from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        if truckSize <= 0:
            return 0
        boxTypes = sorted(boxTypes, key=lambda item: item[1], reverse=True)
        uncount = 0
        remain = truckSize
        for boxes, units in boxTypes:
            uncount += (remain if boxes >= remain else boxes) * units
            remain -= boxes
            if remain <= 0:
                break

        return uncount


if __name__ == "__main__":
    inputs = [
        ([[1, 3], [2, 2], [3, 1]], 4),
        ([[5, 10], [2, 5], [4, 7], [3, 9]], 10)
    ]
    outputs = [
        8,
        91
    ]
    sol = Solution()
    for (nums, k), expected in zip(inputs, outputs):
        res = sol.maximumUnits(nums, k)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
