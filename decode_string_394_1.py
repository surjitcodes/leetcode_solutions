import collections
import sys
import time
import random
import json

def peek(stack):
    if stack: return stack[-1]


class Solution:
    def decodeString(self, s):
        print(s)

        stack = []

        for i in range(len(s)):
            print(stack)
            if s[i] != ']':
                stack.append(s[i])
            else:
                decoded_part = []

                # get the encoded string
                while peek(stack) != '[':
                    decoded_part.append(stack.pop())
                stack.pop()   # pop [ from the stack

                # get rpt factor
                base = 1
                rpt_count = 0
                while peek(stack) and '0' <= peek(stack) <= '9':
                    rpt_count += (int(stack.pop())) * base
                    base *= 10

                # push decoded_string rpt times into stack
                for _ in range(rpt_count):
                    for j in range(len(decoded_part) - 1, -1, -1):
                        stack.append(decoded_part[j])

        return "".join(stack)


input = "2[ab]2[c3[d]]"
sol = Solution()
result = sol.decodeString(input)
print(result)
