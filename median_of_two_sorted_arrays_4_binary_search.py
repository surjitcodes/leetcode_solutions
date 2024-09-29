import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def findMedianSortedArrays(self, A, B) -> float:
        m, n = len(A), len(B)
        count = m + n

        def get_val(target_pos, st1, end1, st2, end2):
            if st1 > end1:                 # segment 1 is empty
                return B[target_pos - st1]     # pass element of 2
            if st2 > end2:                 # segment 2 is empty
                return A[target_pos - st2]     # pass element of 1

            # Get middle indexes and middle values of A and B
            mid1, mid2 = (st1 + end1) // 2, (st2 + end2) // 2
            val1, val2 = A[mid1], B[mid2]

            if mid1 + mid2 < target_pos:    # curtail smaller left half.
                if val1 < val2:     # shift st1
                    return get_val(target_pos, mid1 + 1, end1, st2, end2)
                else:               # shift st2
                    return get_val(target_pos, st1, end1, mid2 + 1, end2)

            else:           # Otherwise, curtail the larger right half.
                if val1 < val2:     # shift end2
                    return get_val(target_pos, st1, end1, st2, mid2 - 1)
                else:               # shift end1
                    return get_val(target_pos, st1, mid1 - 1, st2, end2)

        if count % 2:
            return get_val(count // 2, 0, m - 1, 0, n - 1)
        else:
            return (get_val(count // 2 - 1, 0, m - 1, 0, n - 1)
                    + get_val(count // 2, 0, m - 1, 0, n - 1)) / 2


nums1 = [1, 1, 2, 4]
nums2 = [2, 3, 4, 6, 7]
sol = Solution()
result = sol.findMedianSortedArrays(nums1, nums2)
print(result)
