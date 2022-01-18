from typing import List
import sys

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                max_profit += prices[i] - prices[i-1]

        return max_profit

    def maxProfitTracking(self, prices: List[int]) -> int:

        profit = 0
        valey, peak = prices[0], prices[0]
        for p in prices[1:]:
            if p < peak:
                profit += peak - valey
                peak = p
                valey = p
            elif p > valey and peak < p:
                peak = p
        
        return profit + peak - valey


if __name__ == "__main__":
    inputs = [
        [7,1,5,3,6,4],
        [1,2,3,4,5],
        [7,6,4,3,1],
        [3,3,5,0,0,3,1,4]
    ]
    expected_list = [
        7,
        4,
        0,
        6
    ]
    sol = Solution()
    for prices, expected in zip(inputs, expected_list):
        output = sol.maxProfit(prices)
        assert output == expected, f'{output} while expected {expected}'