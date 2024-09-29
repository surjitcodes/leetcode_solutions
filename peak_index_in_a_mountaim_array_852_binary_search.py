import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            print(mid)

            if arr[mid] < arr[mid + 1]: # mid to mid+1 Segment Left
                left = mid + 1
            else:                       # mid to mid+1 Segment Right
                right = mid

        return left


a = [1, 2, 4, 5, 7, 8, 9, 6, 3]
a = [1, 2, 7, 8, 3]
print(a)
sol = Solution()
result = sol.peakIndexInMountainArray(a)
print(result)
