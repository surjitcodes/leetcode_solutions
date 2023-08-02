import collections
import sys
import time
import random
import json


from collections import defaultdict



class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        nr = len(grid)
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    grid[r][c] = '0'    # mark as visited
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()  # BFS
                        if row-1 >= 0 and grid[row-1][col] == '1':
                            neighbors.append((row-1, col))
                            grid[row-1][col] = '0'
                        if col-1 >= 0 and grid[row][col-1] == '1':
                            neighbors.append((row, col-1))
                            grid[row][col-1] = '0'
                        if row+1 < nr and grid[row+1][col] == '1':
                            neighbors.append((row+1, col))
                            grid[row+1][col] = '0'
                        if col+1 < nc and grid[row][col+1] == '1':
                            neighbors.append((row, col+1))
                            grid[row][col+1] = '0'

        return num_islands

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
