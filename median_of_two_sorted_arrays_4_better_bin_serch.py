import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def findMedianSortedArrays(self, A, B) -> float:
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        print(A, B)

        m, n = len(A), len(B)
        left, right = 0, m

        while left <= right:
            midA = (left + right) // 2
            midB = (m + n + 1) // 2 - midA
            print(midA, midB)

            max_leftA = float('-inf') if midA == 0 else A[midA - 1]
            max_leftB = float('-inf') if midB == 0 else B[midB - 1]
            min_rightA = float('inf') if midA == m else A[midA]
            min_rightB = float('inf') if midB == n else B[midB]

            if max_leftA <= min_rightB and max_leftB <= min_rightA:
                if (m + n) % 2 == 1:
                    return max(max_leftA, max_leftB)
                else:
                    return (max(max_leftA, max_leftB)
                            + min(min_rightA, min_rightB)) / 2
            elif max_leftA > min_rightB:
                right = midA - 1
            else:
                left = midA + 1


A = [1, 1, 2, 4]
A = [2, 4, 5, 6]
B = [2, 3, 4, 6, 7]
B = [1, 2, 3, 3, 8]
sol = Solution()
result = sol.findMedianSortedArrays(A, B)
print(result)
