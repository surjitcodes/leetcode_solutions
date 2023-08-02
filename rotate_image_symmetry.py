import sys
import time
import random
import json

from collections import Counter
from itertools import zip_longest

from past.builtins import xrange


class Solution:
    def transpose(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(i + 1, n):
                mat[j][i], mat[i][j] = mat[i][j], mat[j][i]

    def reflect(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(n // 2):
                mat[i][j], mat[i][-j - 1] = mat[i][-j - 1], mat[i][j]

    def rotate(self, mat: list[list[int]]) -> None:
        self.transpose(mat)
        self.reflect(mat)


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
    mat = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.rotate(mat)
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)
    print(mat)


if __name__ == "__main__":
    main()
