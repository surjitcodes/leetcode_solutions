import collections
import sys
import time
import random
import json

class Solution:
    def removeStones(self, stones):
        def are_adjacent(a, b):
            return a[0] == b[0] or a[1] == b[1]

        # Returns the representative of vertex x
        def find_representative(x):
            if x == rep[x]:
                return x
            # Uses Path compression
            return find_representative(rep[x])

        # Combine stones x and y
        def perform_union(x, y):
            rx = find_representative(x)
            ry = find_representative(y)
            if rx == ry:
                return False

            if size[rx] < size[ry]:
                rep[rx] = ry
                size[ry] += size[rx]
            else:
                rep[ry] = rx
                size[rx] += size[ry]
            return True  # Two components merged

        # Initialize rep to itself and size as 1
        rep = [i for i in range(len(stones))]
        size = [1 for _ in range(len(stones))]
        component_count = len(stones)

        for i in range(len(stones)):
            for j in range(i+1, len(stones)):

                if are_adjacent(stones[i], stones[j]):
                    # Decrease comp if merging performed
                    if perform_union(i, j):
                        component_count -= 1

        # Return the maximum stone that can be removed
        return len(stones) - component_count


input = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [3, 3]]
sol = Solution()
result = sol.removeStones(input)
print(result)
