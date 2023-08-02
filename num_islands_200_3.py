import collections
import sys
import time
import random
import json


from collections import defaultdict

class UnionFind:
    def __init__(self, grid):
        #print(grid)
        m = len(grid)
        #self.n =
        n = len(grid[0])
        self.count = 0
        self.parent = [0 for i in range(m*n)]
        self.rank = [0 for i in range(m*n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i*n + j] = i*n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

            self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        nr = len(grid)
        nc = len(grid[0])

        uf = UnionFind(grid)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':

                    grid[r][c] = '0'   # Optional

                    if r - 1 >= 0 and grid[r-1][c] == '1':
                        uf.union(r * nc + c, (r-1) * nc + c)
                    if r + 1 < nr and grid[r+1][c] == '1':
                        uf.union(r * nc + c, (r+1) * nc + c)
                    if c - 1 >= 0 and grid[r][c-1] == '1':
                        uf.union(r * nc + c, r * nc + c - 1)
                    if c + 1 < nc and grid[r][c+1] == '1':
                        uf.union(r * nc + c, r * nc + c + 1)

        return uf.get_count()


def execution_time(start_time):
    return int((time.time() - start_time) * 1.0e6)
    # return f"{method} {(time.time() - start_time) * 1.0e6:.03f}"


def gen_save_rand_list(count, limit):
    nums = random.sample(range(1, limit), count)
    with open('random_data.json', 'w') as f:
        json.dump(nums, f)


def read_rand_list() -> int:
    with open('random_data.json') as json_file:
        json_data = json.load(json_file)
        #  json_data.sort()
    return json_data


def main():
    """
    grid = [
        ['0', '1', '1'],
        ['1', '1', '0'],
        ['0', '0', '1'],
        ['1', '0', '1']
        ]
    """
    grid = [
        ['0', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '1'],
        ['0', '0', '1', '0', '1'],
        ['1', '1', '0', '1', '1'],
        ['0', '1', '1', '1', '0'],
        ['0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '0']
        ]

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.numIslands(grid)
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
