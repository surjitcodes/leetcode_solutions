import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        def build_graph(intervals):
            #  To be expanded

            def overlap(a, b):
                return a[0] <= b[1] and b[0] <= a[1]

            graph = collections.defaultdict(list)
            for i, interval_i in enumerate(intervals):
                for j in range(i + 1, len(intervals)):
                    if overlap(interval_i, intervals[j]):
                        graph[tuple(interval_i)].append(intervals[j])
                        graph[tuple(intervals[j])].append(interval_i)
            return graph

        def get_components(graph, intervals):
            #  To be expanded
            visited = set()
            n_comp = 0
            nodes_in_comp = collections.defaultdict(list)

            def mark_component_DFS(start):
                stack = [start]
                while stack:
                    node = tuple(stack.pop())
                    if node not in visited:
                        visited.add(node)
                        nodes_in_comp[n_comp].append(node)
                        stack.extend(graph[node])

            for interval in intervals:
                if tuple(interval) not in visited:
                    mark_component_DFS(interval)
                    n_comp += 1
            return nodes_in_comp, n_comp

        def merge_nodes(nodes):
            #  To be expanded
            start_interval = min(node[0] for node in nodes)
            end_interval = max(node[1] for node in nodes)
            return [start_interval, end_interval]

        graph = build_graph(intervals)
        print(graph)
        nodes, n_comp = get_components(graph, intervals)
        return [merge_nodes(nodes[comp]) for comp in range(n_comp)]


a = [[1, 3], [2, 6], [15, 18], [6, 10]]
sol = Solution()
result = sol.merge(a)
print(result)
