import collections
import sys
import time
import random
import json

class Solution:
    def removeStones(self, stones):

        def are_adjacent(a, b):
            return a[0] == b[0] or a[1] == b[1]

        def dfs(current_stone):
            visited[current_stone] = True

            # Iterate over all unvisited neighbors
            for adjacent in edge[current_stone]:
                if not visited[adjacent]:
                    dfs(adjacent)

        edge = [[] for _ in range(len(stones))]
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if are_adjacent(stones[i], stones[j]):
                    edge[i].append(j)
                    edge[j].append(i)

        visited = [False for _ in range(len(stones))]
        connected_components = 0
        for i in range(len(stones)):
            if not visited[i]:
                connected_components += 1
                dfs(i)

        return len(stones) - connected_components


input = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 0], [3, 3]]
sol = Solution()
result = sol.removeStones(input)
print(result)
