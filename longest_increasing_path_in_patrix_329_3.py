import sys
import time
import random
import json


class Solution:
    def __init__(self):
        self.m = self.n = None
        self.dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def longestIncreasingPath(self, matrix):
        if not matrix or len(matrix) == 0: return 0
        self.m = len(matrix)
        self.n = len(matrix[0])

        # Padding sup_mat with zero as boundaries (assume all +ve)
        sup_mat = [[0 for x in range(self.n+2)]]
        for x in range(self.m):
            sup_mat.append([0]+matrix[x]+[0])
        sup_mat.append([0 for x in range(self.n+2)])
        self.m += 2
        self.n += 2

        # Calculate out_degrees
        out_degree = [[0 for x in range(self.n)]
                     for y in range(self.m)]

        for x in range(1, self.m-1):
            for y in range(1, self.n-1):
                for dx, dy in self.dir:
                    if sup_mat[x][y] < sup_mat[x+dx][y+dy]:
                        out_degree[x][y] += 1

        # List of leaves
        leaves = []
        for x in range(1, self.m-1):
            for y in range(1, self.n-1):
                if out_degree[x][y] == 0:
                    leaves.append((x, y))

        height = 0
        while len(leaves) > 0:
            height += 1
            new_leaves = []
            for x, y in leaves:

                for dx, dy in self.dir:
                    xx = x + dx
                    yy = y + dy

                    if sup_mat[x][y] > sup_mat[xx][yy]:
                        out_degree[xx][yy] -= 1
                        if out_degree[xx][yy] == 0:
                            new_leaves.append((xx, yy))
            print(height)
            print(new_leaves)
            print(out_degree)
            leaves = new_leaves

        print(out_degree)
        return height


matrix = [[9, 3, 4],
        [6, 6, 8],
        [2, 1, 1]]

sol = Solution()
result = sol.longestIncreasingPath(matrix)
print(result)
