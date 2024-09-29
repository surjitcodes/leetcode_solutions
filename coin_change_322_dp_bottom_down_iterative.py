import collections
import itertools
import sys
import time
import random
import json


class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:

            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


coins = [1, 2, 5]
amount = 11
print(coins, amount)
sol = Solution()
result = sol.coinChange(coins, amount)
print(result)
