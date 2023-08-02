import sys
import time
import random
import json

from collections import Counter
from enum import Enum
from itertools import zip_longest

from past.builtins import xrange


class Solution:
    def canJump(self, nums: list[int]):
        # Set the initial goal position
        goal_pos = len(nums) - 1

        # Run a loop from second last position down to start
        for pos in range(goal_pos - 1, -1, -1):

            # Can we reach the goal from this position
            if pos + nums[pos] >= goal_pos:

                # Shift the goal position
                goal_pos = pos

        # Has the goal moved to the starting position
        return goal_pos == 0


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
    nums = [2, 4, 0, 1, 3]
    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.canJump(nums)
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
