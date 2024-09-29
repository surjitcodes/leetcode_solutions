import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def insertInterval(self, intervals, new_interval):

        print(intervals, new_interval)

        left, right = 0, len(intervals)

        while left < right:
            mid = (left + right) // 2
            if new_interval[0] <= intervals[mid][0]:
                right = mid
            else:
                left = mid + 1
            # print(left, right, mid)

        pos = left
        print(pos)

        intervals.insert(pos, new_interval)

        if pos > 0 and intervals[pos-1][1] >= intervals[pos][0]:
            print("previous also merging")
            pos -= 1

        print(intervals, pos)

        while pos+1 < len(intervals) \
                and intervals[pos][1] >= intervals[pos+1][0]:
            intervals[pos][1] = max(intervals[pos][1], intervals[pos+1][1])
            intervals.pop(pos+1)
            print(intervals, pos)

        return intervals


a = [[1, 2], [3, 5], [7, 8], [9, 10], [12, 16]]
b = [24, 29]
sol = Solution()
result = sol.insertInterval(a, b)
print(result)
