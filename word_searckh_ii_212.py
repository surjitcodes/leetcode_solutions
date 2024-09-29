import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]):
        # build trie of words
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})  # retrieve node
            node[WORD_KEY] = word  # mark existence of word in trie

        n_rows = len(board)
        n_col = len(board[0])
        matched_words = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            node = parent[letter]

            word_match = node.pop(WORD_KEY, False)  # check word match
            if word_match:  # match found? remove matched word without set use
                matched_words.append(word_match)

            board[row][col] = '#'  # mark as visited

            for (row_offset, col_offset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + row_offset, col + col_offset
                if not (0 <= new_row < n_rows and 0 <= new_col < n_col):
                    continue
                if not board[new_row][new_col] in node:
                    continue
                backtracking(new_row, new_col, node)
            board[row][col] = letter  # End of EXPLORATION, we restore the cell

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not node:
                parent.pop(letter)

        for row in range(n_rows):
            for col in range(n_col):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matched_words


board = [["h","a","o","n"],["e","t","x","d"],["i","h","g","o"],["i","f","s","d"]]
words = ["dig", "oath", "dog", "dogs"]
sol = Solution()
result = sol.findWords(board, words)
print(result)
