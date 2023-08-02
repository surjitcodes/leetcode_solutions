import sys
import time
import random
import json


class Solution:
    def __init__(self):
        self.m = None
        self.n = None
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def longestIncreasingPath(self, matrix):
        if not matrix or len(matrix) == 0: return 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        ans = 0

        for r in range(self.m):
            for c in range(self.n):
                ans = max(ans, self.dfs(matrix, r, c))
        return ans

    def dfs(self, matrix, i, j):
        ans = 0
        for dx, dy in self.dirs:
            x = i + dx
            y = j + dy
            if 0 <= x < self.m and 0 <= y < self.n \
                    and matrix[x][y] > matrix[i][j]:
                ans = max(ans, self.dfs(matrix, x, y))
        return ans + 1


matrix = [[9, 3, 4],
          [6, 6, 8],
          [2, 1, 1]]

sol = Solution()
result = sol.longestIncreasingPath(matrix)
print(result)
