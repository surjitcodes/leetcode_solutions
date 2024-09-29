import collections
import itertools
import sys
import time
import random
import json



class Solution:
    def numberOfPatterns(self, m: int, n: int):

        def is_valid(last_index, index):
            if last_index == -1:
                return True  # first digit of pattern
            if used[index]:
                return False
            if (index + last_index) % 2 == 1:  # knight moves or adj cells
                return True

            mid = (index + last_index) // 2  # diagonals 0,0 & 8,8 or 0,8 & 8,0
            if mid == 4:
                return used[mid]
            # adjacent cells on diagonal, e.g. 0,0 & 1,0 or 2,0 & 1,1
            if (index % 3 != last_index % 3) \
                    and (index // 3 != last_index // 3):
                return True
            return used[mid]  # all other cells which are not adjacent

        def calc_patterns(len, last_index=-1):
            if len == 0:
                return 1

            sum = 0
            for index in range(9):
                if is_valid(last_index, index):
                    used[index] = True
                    sum += calc_patterns(len - 1, index)
                    used[index] = False
            return sum

        used = [False for i in range(9)]
        result = 0
        for len in range(m, n+1):
            result += calc_patterns(len)
        return result


sol = Solution()
result = sol.numberOfPatterns(1, 2)
print(result)
