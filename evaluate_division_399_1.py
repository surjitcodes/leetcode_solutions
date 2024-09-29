import collections
import sys
import time
import random
import json

class Solution:
    def calcEquation(self, equations, values, queries):
        print(equations, values, queries)
        graph = collections.defaultdict(collections.defaultdict)

        # Build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        def dfs(curr_nd, trgt_nd, prod, visited):
            visited.add(curr_nd)
            ret = -1.0
            neighbors = graph[curr_nd]
            if trgt_nd in neighbors:
                ret = prod * neighbors[trgt_nd]
            else:
                for neighbor, val in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = dfs(neighbor, trgt_nd, prod * val, visited)
                    if ret != -1.0:
                        break
            visited.remove(curr_nd)
            return ret

        # Evaluate queries-DFS. Verify path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1.0  # At least one node does not exist
            elif dividend == divisor:
                ret = 1.0  # origin and destination is same node
            else:
                ret = dfs(dividend, divisor, 1, set())
            results.append(ret)

        return results


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

sol = Solution()
result = sol.calcEquation(equations, values, queries)
print(result)
