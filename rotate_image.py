import sys
import time
import random
import json

from collections import Counter
from itertools import zip_longest

from past.builtins import xrange


class Solution:
    def rotate(self, mat: list[list[int]]) -> None:
        n = len(mat[0])
        last = n - 1

        for i in range((n+1) // 2):
            for j in range(n // 2):
                temp = mat[i][j]
                mat[i][j] = mat[last - j][i]
                mat[last - j][i] = mat[last - i][last - j]
                mat[last - i][last - j] = mat[j][last - i]
                mat[j][last - i] = temp


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
    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.rotate(matrix)
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)
    print(matrix)


if __name__ == "__main__":
    main()
