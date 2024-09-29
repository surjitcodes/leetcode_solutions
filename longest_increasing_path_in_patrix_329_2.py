import sys
import time
import random
import json


class Solution:
    def __init__(self):
        self.m = self.n = self.memo = None
        self.dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def longestIncreasingPath(self, matrix):
        if not matrix or len(matrix) == 0: return 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.memo = [[0 for x in range(self.m)]
                     for y in range(self.n)]
        ans = 0

        for x in range(self.m):
            for y in range(self.n):
                ans = max(ans, self.dfs(matrix, x, y))

        return ans

    def dfs(self, matrix, x, y):
        if self.memo[x][y] != 0: return self.memo[x][y]
        for dx, dy in self.dir:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < self.m and 0 <= yy < self.n \
                    and matrix[xx][yy] > matrix[x][y]:
                self.memo[x][y] = max(self.memo[x][y],
                                      self.dfs(matrix, xx, yy))
        self.memo[x][y] += 1
        return self.memo[x][y]


matrix = [[9, 3, 4],
          [6, 6, 8],
          [2, 1, 1]]

sol = Solution()
result = sol.longestIncreasingPath(matrix)
print(result)
