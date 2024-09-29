import collections
import itertools
import sys
import time
import random
import json


class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:

        def dfs(rem):
            if rem < 0:
                return -1

            if rem == 0:
                return 0

            min_cost = float('inf')

            for coin in coins:
                res = dfs(rem - coin)

                if res != -1:
                    min_cost = min(min_cost, res + 1)
                    
            return min_cost if min_cost != float('inf') else -1

        return dfs(amount)


coins = [1, 2, 5]
amount = 11
print(coins, amount)
sol = Solution()
result = sol.coinChange(coins, amount)
print(result)
