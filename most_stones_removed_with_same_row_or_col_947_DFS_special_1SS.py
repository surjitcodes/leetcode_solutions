import collections
import sys
import time
import random
import json


class Solution:
    def removeStones(self, stones):
        k = 10001

        def dfs(current_node):
            visited[current_node] = True
            # Iterate over all unvisited neighbors
            for adjacent in edge[current_node]:
                if not visited[adjacent]:
                    dfs(adjacent)

        edge = [[] for _ in range(2*k)]
        for i in range(len(stones)):
            x = stones[i][0]
            y = stones[i][1] + k
            edge[x].append(y)
            edge[y].append(x)

        visited = [False for i in range(2*k)]
        connected_components = 0
        for i in range(2*k):
            if not visited[i] and len(edge[i]) > 0:
                connected_components += 1
                dfs(i)

        return len(stones) - connected_components


input = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [3, 3]]
sol = Solution()
result = sol.removeStones(input)
print(result)
