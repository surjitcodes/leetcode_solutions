import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def wordSquares(self, words: list[str]) -> list[list[str]]:
        print(words)

        def get_words_with_prefix(prefix):
            for word in words:
                if word.startswith(prefix):
                    yield word

        def backtracking(step):
            print(step)
            if step == n:
                results.append(word_square[:])
                print(results)
                return

            prefix = ''.join([word[step] for word in word_square])
            # find out all words that start with the given prefix
            for candidate in get_words_with_prefix(prefix):
                print(candidate)
                # iterate row by row
                word_square.append(candidate)
                print("WS", word_square)
                backtracking(step + 1)
                word_square.pop()

        n = len(words[0])
        results = []
        for word in words:
            print("Word", word)
            # try with every word as the starting word
            word_square = [word]
            backtracking(1)
        return results


words = ["area", "lead", "wall", "lady", "ball"]
sol = Solution()
result = sol.wordSquares(words)
print(result)
