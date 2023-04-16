import sys
import time
import random
import json


class Solution:
    def NextPermutation(self, nums: list[int]) -> None:

        def reverse(start):
            i = start
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # Find the pivot position
        pivot = len(nums) - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot+1]:
            pivot -= 1

        # If pivot is found, find its replacement
        if pivot >= 0:
            # Find position of its replacement
            pos = len(nums) - 1
            while nums[pos] <= nums[pivot]:
                pos -= 1

            # Swap the pivot with replacement number
            nums[pivot], nums[pos] = nums[pos], nums[pivot]

        # Reverse numbers to the right of pivot
        reverse(pivot+1)



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
    nums = [9, 2, 3, 6, 5, 1]
    print(nums[:20])

    n = 1

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.NextPermutation(nums)
        ex_time = execution_time(start_time)
        total += ex_time
        # result1 = f'{len(result):9} {total // n: 5d}'
    # print(result1, end='')

    print('\n')
    # print(result)
    print(nums)


if __name__ == "__main__":
    main()
