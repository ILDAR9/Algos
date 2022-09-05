from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
        	return -1
        res = 0
        total = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
        	total += g-c
        	if total < 0:
        		res = i+1
        		total = 0

        return res


if __name__ == "__main__":
    inputs = [
        ([1,2,3,4,5], [3,4,5,1,2]),
        ([2,3,4], [3,4,3])
    ]
    outputs = [
        3,
        -1
    ]

    sol = Solution()
    for (gas, cost), expected in zip(inputs, outputs):
        res = sol.canCompleteCircuit(gas, cost)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')