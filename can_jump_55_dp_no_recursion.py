import sys
import time
import random
import json

from collections import Counter
from enum import Enum
from itertools import zip_longest

from past.builtins import xrange


class Status(Enum):
    Good = 1
    Bad = 2


class Solution:
    def canJump(self, nums: list[int]):

        n = len(nums)
        status = [Status.Bad]*n
        status[n-1] = Status.Good

        # Run a loop from second last position down to start
        for pos in range(n-2, -1, -1):

            # Find farthest pos reachable from pos
            furthest_jump_pos = min(pos + nums[pos], n - 1)

            # Inspect all positions reachable from pos
            for next_pos in range(pos+1, furthest_jump_pos+1):

                # If anyone of these is Good then pos is Good
                if status[next_pos] == Status.Good:
                    status[pos] = Status.Good
                    break

        # If starting pos is Good solution is True otherwise False
        return status[0] == Status.Good


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
