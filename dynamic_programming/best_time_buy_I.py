from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = sys.maxsize, 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == "__main__":
    inputs = [
        [7,1,5,3,6,4],
        [7,6,4,3,1],

    ]
    expected_list = [
        5,
        0
    ]
    sol = Solution()
    for prices, expected in zip(inputs, expected_list):
        output = sol.maxProfit(prices)
        assert output == expected, f'{output} while expected {expected}'