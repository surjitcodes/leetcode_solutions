import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:


        final_n = n
        reversible_pairs = [
            ['0', '0'], ['1', '1'],
            ['6', '9'], ['8', '8'], ['9', '6']
        ]

        def generate_strobo_numbers(n):
            if n == 0:
                # 0-digit strobogrammatic number is empty.
                return [""]

            if n == 1:
                # 1-digit strobogrammatic numbers.
                return ["0", "1", "8"]

            prev_result = generate_strobo_numbers(n - 2)
            result = []

            for prev_num in prev_result:
                for pair in reversible_pairs:
                    if pair[0] != '0' or n != final_n:
                        result.append(pair[0] + prev_num + pair[1])

            return result

        return generate_strobo_numbers(final_n)


n = 3
sol = Solution()
result = sol.findStrobogrammatic(n)
print(result)
