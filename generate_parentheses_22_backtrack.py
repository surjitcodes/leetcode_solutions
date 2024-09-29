import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def backtracking(left_count, right_count):
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))
                return

            if left_count < n:
                cur_string.append("(")
                backtracking(left_count + 1, right_count)
                cur_string.pop()

            if right_count < left_count:
                cur_string.append(")")
                backtracking(left_count, right_count + 1)
                cur_string.pop()

        answer = []
        cur_string = []
        backtracking(0, 0)
        return answer


sol = Solution()
result = sol.generateParenthesis(2)
print(result)
