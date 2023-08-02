import sys
import time
import random
import json

from collections import Counter
from enum import Enum
from itertools import zip_longest

from past.builtins import xrange


class Status(Enum):
    Unknown = 0
    Good = 1
    Bad = 2

status = []

class Solution:
    def can_jump_from(self, pos: int, nums: list[int]) -> bool:
        if status[pos] == Status.Good: return True
        elif status[pos] == Status.Bad: return False

        furthest_jump_pos = min(pos + nums[pos], len(nums) - 1)

        for next_pos in range(pos+1, furthest_jump_pos+1):
            obj = Solution()
            if obj.can_jump_from(next_pos, nums):
                status[next_pos] = Status.Good
                return True
            
        status[pos] = Status.Bad
        return False

    def canJump(self, nums: list[int]):
        n = len(nums)
        for i in range(n): status.append(Status.Unknown)
        status[n-1] = Status.Good

        obj = Solution()
        return obj.can_jump_from(0, nums)



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
