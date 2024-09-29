import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def merge(self, intervals) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:

            # merged list is empty, or current interval does
            # not overlap with recently saved interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:  # overlap: current & recently saved interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


a = [[1, 3], [2, 6], [15, 18], [6, 10]]
sol = Solution()
result = sol.merge(a)
print(result)
