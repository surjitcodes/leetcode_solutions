import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        letters = {"2": "abc", "3": "def", "4": "ghi",
                   "5": "jkl", "6": "mno", "7": "pqrs",
                   "8": "tuv", "9": "wxyz"}

        def backtrack(index):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            possible_letters = letters[digits[index]]

            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                backtrack(index + 1)  # Move on to next digit
                path.pop()  # Backtrack by removing letter

        combinations = []
        # Initiate backtracking with an empty path and index 0
        path = []
        backtrack(0)
        return combinations


sol = Solution()
result = sol.letterCombinations('23')
print(result)
