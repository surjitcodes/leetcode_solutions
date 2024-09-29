import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            ans = [left, left]

            while left >= 0 and right < len(s) \
                    and s[left] == s[right]:
                ans = [left, right]
                left -= 1
                right += 1
            return ans

        best_ans = [0, 0]

        for mid in range(len(s)):
            #  Odd length palindromic substring
            new_ans = expand(mid, mid)
            if new_ans[1] - new_ans[0] > best_ans[1] - best_ans[0]:
                best_ans = new_ans

            #  Even length palindromic substring
            new_ans = expand(mid, mid + 1)
            if new_ans[1] - new_ans[0] > best_ans[1] - best_ans[0]:
                best_ans = new_ans

        return s[best_ans[0]: best_ans[1]+1]


a = "aabacbcaa"
print(a)
sol = Solution()
result = sol.longestPalindrome(a)
print(result)
