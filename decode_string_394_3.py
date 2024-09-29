import collections
import sys
import time
import random
import json


class Solution:
    def __init__(self):
        self.pos = 0

    def decodeString(self, s):
        result = ""

        while self.pos < len(s) and s[self.pos] != ']':
            if not ('0' <= s[self.pos] <= '9'):
                result += s[self.pos]
                self.pos += 1
            else:
                rpt_count = 0
                # build rpt_count while next character is a digit
                while self.pos < len(s) and '0' <= s[self.pos] <= '9':
                    rpt_count = rpt_count*10 + int(s[self.pos])
                    self.pos += 1
                # ignore the opening bracket '['
                self.pos += 1

                decoded_string = self.decodeString(s)
                # ignore the closing bracket ']'
                self.pos += 1

                # add decoded_string rpt_count times
                for _ in range(rpt_count):
                    result += decoded_string

        return result


input = "2[ab]2[c3[d]]"
sol = Solution()
result = sol.decodeString(input)
print(result)
