import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return [""]

        answer = []
        for left_count in range(n):
            for left_string in self.generateParenthesis(left_count):
                for right_string in self.generateParenthesis(n - 1 - left_count):
                    answer.append("(" + left_string + ")" + right_string)

        return answer


sol = Solution()
result = sol.generateParenthesis(2)
print(result)
