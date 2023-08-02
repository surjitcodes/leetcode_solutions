import collections
import sys
import time
import random
import json


from collections import defaultdict



class Solution:
    def __init__(self):
        self.nr = None
        self.nc = None

    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        self.nr = len(grid)
        self.nc = len(grid[0])

        num_islands = 0
        for r in range(self.nr):
            for c in range(self.nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands

    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        if r-1 >= 0 and grid[r-1][c] == '1':
            self.dfs(grid, r-1, c)
        if c-1 >= 0 and grid[r][c-1] == '1':
            self.dfs(grid, r, c-1)
        if r+1 < self.nr and grid[r+1][c] == '1':
            self.dfs(grid, r+1, c)
        if c+1 < self.nc and grid[r][c+1] == '1':
            self.dfs(grid, r, c+1)


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
