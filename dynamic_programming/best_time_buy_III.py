from typing import List
import sys

class Solution:

    def maxProfit(self, prices):
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

    def maxProfitDoubleDP(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        len_price = len(prices)
        min_price, max_profit = prices[0], 0
        max_price, max_profit_right = prices[-1], 0
        left_profits = [0] * len_price
        rights_profits = [0] * (len_price+1)
        for i, (price, right_price) in enumerate(zip(prices[1:], prices[:0:-1]), start=1):
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            left_profits[i] = max_profit

            max_price = max(max_price, right_price)
            max_profit_right = max(max_profit_right, max_price - right_price)
            rights_profits[len_price - i] = max_profit_right

        return max((left_profits[i] + rights_profits[i+1] for i in range(len_price)))

if __name__ == "__main__":
    inputs = [
        [1,2,4,2,5,7,2,4,9,0],
        [3,3,5,0,0,3,1,4],
        [1,2,3,4,5],
        [7,6,4,3,1]
    ]
    expected_list = [
        13,
        6,
        4,
        0
    ]
    sol = Solution()
    for prices, expected in zip(inputs, expected_list):
        output = sol.maxProfit(prices)
        assert output == expected, f'{output} while expected {expected}'
        print('done')