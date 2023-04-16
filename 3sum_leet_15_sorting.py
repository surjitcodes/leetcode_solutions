import sys
import time
import random
import json


class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:  # It is first element or non-duplicate
                self.two_sum_sorted(nums, i, output)

        return output

    def two_sum_sorted(self, nums: list[int], i: int, output: list[list[int]]):
        low, high = i + 1, len(nums) - 1
        while low < high:
            sum = nums[i] + nums[low] + nums[high]
            if sum < 0:
                low += 1
            elif sum > 0:
                high -= 1
            else:
                output.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low-1]:
                    low += 1


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
    nums = read_rand_list()

    i = 0
    while i < len(nums):
        nums[i] = -nums[i]
        i += 2

    # nums = [-2, -1, -1, -1, -1, 0, 0, 0, 0, 1, 2, 4]
    nums = [5, 4, 5, 3, -7, 4, 0, -8, 2, -7, -2]

    print(nums[:20])

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.three_sum(nums)
    print(result)
    output = f'Count = {len(result)} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
