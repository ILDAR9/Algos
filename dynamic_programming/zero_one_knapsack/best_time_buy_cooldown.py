from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = dict()
        def dfs(i: int, is_buy: bool):
            if i >= len(prices):
                return 0
            k = (i, is_buy)
            if k in dp:
                return dp[k]

            cooldown = dfs(i+1, is_buy)
            if is_buy:
                buy = dfs(i+1, False) - prices[i]
                dp[k] = max(buy, cooldown)
            else:
                sell = dfs(i+2, True) + prices[i]
                dp[k] = max(sell, cooldown)
            return dp[k]

        return dfs(0, True)



if __name__ == "__main__":
    inputs = [
        [1,2,3,0,2],
        [1]

    ]
    expected_list = [
        3,
        0
    ]
    sol = Solution()
    for prices, expected in zip(inputs, expected_list):
        output = sol.maxProfit(prices)
        assert output == expected, f'{output} while expected {expected}'
        print('pass')