import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def isAnagram(self, a: str, b: str) -> bool:

        print(a, b)

        if len(a) != len(b):
            return False

        char_a = [*a]
        char_b = list(b)

        char_a = []
        char_a.extend(a)

        print(char_a, char_b)

        sorted_char_a = sorted(char_a)
        sorted_char_b = sorted(char_b)

        print(sorted_char_a, sorted_char_b)
        return sorted_char_a == sorted_char_b


a = "anagram"
b = "nagaram"
sol = Solution()
result = sol.isAnagram(a, b)
print(result)
