import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        reversible_pairs = [
            ['0', '0'], ['1', '1'],
            ['6', '9'], ['8', '8'], ['9', '6']
        ]

        # When n is odd starting string string length 1 else 0
        curr_string_len = n % 2
        nums = ["0", "1", "8"] if curr_string_len == 1 else [""]

        while curr_string_len < n:
            curr_string_len += 2
            new_nums = []

            for num in nums:
                for pair in reversible_pairs:
                    if curr_string_len != n or pair[0] != '0':
                        new_nums.append(pair[0] + num + pair[1])

            nums = new_nums

        return nums


n = 3
sol = Solution()
result = sol.findStrobogrammatic(n)
print(result)
