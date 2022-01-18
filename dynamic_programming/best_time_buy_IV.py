from typing import List
import sys

class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        t1_cost, t2_cost = prices[0], prices[0]
        t1_profit, t2_profit = 0, 0

        for price in prices[1:]:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit

if __name__ == "__main__":
    inputs = [
        (2, [2,4,1]),
        (2, [3,2,6,5,0,3])
    ]
    expected_list = [
        2,
        7
    ]
    sol = Solution()
    for (k, prices), expected in zip(inputs, expected_list):
        output = sol.maxProfit(k, prices)
        assert output == expected, f'{output} while expected {expected}'
        print('done')