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

        """
        freq_a = collections.defaultdict(int)
        for ch in a:
            freq_a[ch] += 1

        freq_b = collections.defaultdict(int)
        for ch in b:
            freq_b[ch] += 1
        """

        freq_a = [0 for x in range(26)]
        freq_b = [0 for x in range(26)]
        out = []
        x = [chr(ch + ord('a')) for ch in range(26)]
        print('  '.join(x))


        for ch in a:
            freq_a[ord(ch) - ord('a')] += 1

        for ch in b:
            freq_b[ord(ch) - ord('a')] += 1
        print(freq_a)
        print(freq_b)

        return freq_a == freq_b


a = "anagram"
b = "nagaram"
sol = Solution()
result = sol.isAnagram(a, b)
print(result)
