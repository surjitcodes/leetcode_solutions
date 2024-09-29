import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def findMedianSortedArrays(self, A, B) -> float:
        pos1, pos2 = 0, 0

        def next_min():
            nonlocal pos1, pos2
            if pos1 < len(A) and pos2 < len(B):
                if A[pos1] < B[pos2]:
                    ans = A[pos1]
                    pos1 += 1
                else:
                    ans = B[pos2]
                    pos2 += 1
            elif pos2 == len(B):
                ans = A[pos1]
                pos1 += 1
            else:
                ans = B[pos2]
                pos2 += 1
            return ans

        count = len(A) + len(B)
        if count % 2 == 1:  # count is odd
            for _ in range(count // 2):
                _ = next_min()
            return next_min()
        else:               # count is even
            for _ in range(count // 2 - 1):
                _ = next_min()
            return (next_min() + next_min()) / 2


nums1 = [1, 1, 2, 4]
nums2 = [2, 3, 4, 6, 7]
sol = Solution()
result = sol.findMedianSortedArrays(nums1, nums2)
print(result)
