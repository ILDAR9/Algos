from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1, 7, 30]

        dp = dict() # index of 'days'

        def dfs(i: int) -> int:

            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float('inf')
            for dur, c in zip(durations, costs):
                j = i
                while j < len(days) and days[j] < days[i] + dur:
                    j+=1
                dp[i] = min(dp[i], c + dfs(j))

            return dp[i]

        return dfs(0)


if __name__ == "__main__":
    inputs = [
        ([1,4,6,7,8,20], [2,7,15]),
        ([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])
    ]
    outputs = [
        11,
        17
    ]
    sol = Solution()
    for (days, costs), expected in zip(inputs, outputs):
        res = sol.mincostTickets(days, costs)
        assert res == expected, f"{res} while expected {expected}"
        print("pass")
