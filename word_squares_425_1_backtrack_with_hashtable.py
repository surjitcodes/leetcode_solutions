import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def wordSquares(self, words: list[str]) -> list[list[str]]:

        def get_words_with_prefix(prefix):
            if prefix in prefix_hash_table:
                return prefix_hash_table[prefix]
            else:
                return set([])

        def backtracking(step):
            if step == s:
                results.append(word_square[:])
                return

            prefix = ''.join([word[step] for word in word_square])
            for candidate in get_words_with_prefix(prefix):
                word_square.append(candidate)
                backtracking(step + 1)
                word_square.pop()

        prefix_hash_table = {}
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                prefix_hash_table.setdefault(prefix, set()).add(word)

        print(prefix_hash_table)

        s = len(words[0])
        results = []
        word_square = []
        for word in words:
            word_square = [word]
            backtracking(1)
        return results

    """
    def buildPrefixHashTable(self, words):
        self.prefixHashTable = {}
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                self.prefixHashTable.setdefault(prefix, set()).add(word)
    """


words = ["area", "lead", "wall", "lady", "ball"]
sol = Solution()
result = sol.wordSquares(words)
print(result)
