import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def insertInterval(self, intervals, new_interval):

        def overlap(a, b):
            return a[0] <= b[1] and b[0] <= a[1]

        print(intervals, new_interval)
        if not intervals or intervals[-1][1] < new_interval[0]:
            intervals.append(new_interval)
            return intervals

        if new_interval[1] < intervals[0][0]:
            intervals.insert(0, new_interval)
            return intervals

        left, right = 0, len(intervals) - 1
        print(left, right, (left + right) // 2)

        while left < right:
            mid = (left + right) // 2
            if new_interval[0] <= intervals[mid][0]:
                right = mid
            else:
                left = mid + 1
            print(left, right, mid)

        pos = left
        print(pos)

        if pos > 0 and overlap(intervals[pos-1], new_interval):
            print("previous also merging")
            pos -= 1

        print(pos, new_interval, intervals)
        intervals[pos][0] = min(intervals[pos][0], new_interval[0])
        intervals[pos][1] = max(intervals[pos][1], new_interval[1])
        print(pos, new_interval, intervals, len(intervals))

        while pos+1 < len(intervals) and intervals[pos][1] >= intervals[pos+1][0]:
            intervals[pos][1] = max(intervals[pos][1], intervals[pos+1][1])
            intervals.pop(pos+1)
            # print(pos, new_interval, intervals, len(intervals))

        return intervals


a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
b = [3, 7]
sol = Solution()
result = sol.insertInterval(a, b)
print(result)
