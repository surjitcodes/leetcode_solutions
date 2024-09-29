import collections
import sys
import time
import random
import json


class Solution:
    def calcEquation(self, equations, values, queries):
        gid_weight = {}

        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]

            if group_id != node_id:
                # found inconsistency, trigger chain update
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = \
                    (new_group_id, node_weight * group_weight)
            return gid_weight[node_id]

        def union(dividend, divisor, val):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # merge the two groups together,
                gid_weight[dividend_gid] = \
                    (divisor_gid, val * divisor_weight
                     / dividend_weight)

        for (dividend, divisor), val in zip(equations, values):
            union(dividend, divisor, val)

        results = []
        for (dividend, divisor) in queries:
            if dividend not in gid_weight \
                    or divisor not in gid_weight:
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    results.append(-1.0)
                else:
                    results.append(dividend_weight
                                   / divisor_weight)
        return results


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

sol = Solution()
result = sol.calcEquation(equations, values, queries)
print(result)
