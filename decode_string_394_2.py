import collections
import sys
import time
import random
import json
'''
def peek(stack):
    if stack: return stack[-1]
'''

class Solution:
    def decodeString(self, s):
        print(s)
        count_stack = []
        string_stack = []
        rpt_count = 0
        string_building = ""
        for i in range(len(s)):
            ch = s[i]

            if '0' <= ch <= '9': # ch is a digit
                rpt_count = rpt_count*10 + int(ch)

            elif ch == '[':    # ch is [
                count_stack.append(rpt_count)
                string_stack.append(string_building)
                string_building = ""
                rpt_count = 0

            elif ch == ']':   # ch is ]
                current_count = count_stack.pop()
                temp_string = string_stack.pop()
                for _ in range(current_count):
                    temp_string += string_building
                string_building = temp_string

            else:   # ch is a letter
                string_building += ch

        return string_building


input = "2[ab]2[c3[d]]"
sol = Solution()
result = sol.decodeString(input)
print(result)
