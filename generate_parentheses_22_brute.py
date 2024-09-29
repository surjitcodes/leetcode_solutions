import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def generateParenthesis(self, n: int):

        def is_valid(p_string):
            left_unpaired = 0
            for p in p_string:
                if p == '(':
                    left_unpaired += 1
                else:
                    left_unpaired -= 1

                if left_unpaired < 0:
                    return False

            return left_unpaired == 0

        answer = []
        queue = collections.deque([""])
        while queue:
            cur_string = queue.popleft()
            if len(cur_string) == 2 * n:
                if is_valid(cur_string):
                    answer.append(cur_string)
                continue

            queue.append(cur_string + ")")
            queue.append(cur_string + "(")
        return answer


sol = Solution()
result = sol.generateParenthesis(3)
print(result)
