import sys
import time
import random
import json


class Solution:
    def AddOne(self, nums: list[int]) -> list[int]:

        # Scan the digits from unit's place
        for pos in range(len(nums)-1, -1, -1):

            # If the digit is less than 9
            if nums[pos] < 9:
                # Add one to it and problem is solved
                nums[pos] += 1
                return nums

            # else (If digit is 9)
            else:
                # Make it 0, and add one to next place
                nums[pos] = 0

        # If all the digits are 9
        nums = [1] + nums
        return nums


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


def read_rand_list(n: int) -> list[int]:
    nums = random.sample(range(0, n), n)
    return nums

def main():
    nums = read_rand_list(18)
    nums = [1, 2, 3]
    # nums = [9, 9, 9]
    nums = []
    print(nums[:20])

    n = 1

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.AddOne(nums)
        ex_time = execution_time(start_time)
        total += ex_time
        # result1 = f'{len(result):9} {total // n: 5d}'
    # print(result1, end='')

    print('\n')
    print(result)
    print(nums)


if __name__ == "__main__":
    main()
