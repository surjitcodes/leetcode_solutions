import sys
import time
import random
import json


class Solution:
    def three_sum_hash(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # Sorting essential to prevent duplicacy
        output = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:  # It is first element or non-duplicate
                self.two_sum_hash(nums, i, output)

        return output

    def two_sum_hash(self, nums: list[int], i: int, output: list[list[int]]):
        hash_set = set()
        j = i + 1
        while j < len(nums):
            complement = -(nums[i] + nums[j])
            if complement in hash_set:
                output.append([nums[i], complement, nums[j]])
                while j + 1 < len(nums) and nums[j+1] == nums[j]:
                    j += 1

            hash_set.add(nums[j])
            j += 1

    def three_sum_sorted(self, nums: list[int]) -> list[list[int]]:
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

    def three_sum_copy_set(self, nums: list[int]) -> set[tuple[int]]:
        output, processed = set(), set()
        for i, val1 in enumerate(nums):
            if val1 not in processed:
                processed.add(val1)

                seen = set()
                for val2 in nums[i + 1:]:
                    complement = -(val1 + val2)
                    if complement in seen:
                        output.add(tuple(sorted((val1, val2, complement))))
                    seen.add(val2)
        return output

    def three_sum_copy_dict(self, nums: list[int]) -> set[tuple[int]]:
        output, processed = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in processed:
                processed.add(val1)

                for val2 in nums[i + 1:]:
                    complement = -(val1 + val2)
                    if complement in seen and seen[complement] == i:
                        output.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return output

    def three_sum_no_copy_dict(self, nums: list[int]) -> set[tuple[int]]:
        output, processed = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in processed:
                processed.add(val1)

                for j in range(i+1, len(nums)):
                    val2 = nums[j]
                    complement = -(val1 + val2)
                    if complement in seen and seen[complement] == i:
                        output.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return output

    def three_sum_no_copy_set(self, nums: list[int]) -> set[tuple[int]]:
        output, processed = set(), set()
        for i, val1 in enumerate(nums):
            if val1 not in processed:
                processed.add(val1)

                seen = set()
                for j in range(i+1, len(nums)):
                    val2 = nums[j]
                    complement = -(val1 + val2)
                    if complement in seen:
                        output.add(tuple(sorted((val1, val2, complement))))
                    seen.add(val2)
        return output

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
    # nums = [5, 4, 5, 3, -7, 4, 0, -8, 2, -7, -2]
    print(nums[:20])

    print('\n      sorted-hash     sorted 2-ptr    copy-set        copy-dict       no-copy-dict    no-copy-set')
    n = 50

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.three_sum_hash(nums)
        ex_time = execution_time(start_time)
        total += ex_time
        result1 = f'{len(result):9} {total // n: 5d}'
    print(result1, end='')

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.three_sum_sorted(nums)
        ex_time = execution_time(start_time)
        total += ex_time
        result2 = f'{len(result):9} {total // n: 5d}'
    print(result2, end='')

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.three_sum_copy_set(nums)
        ex_time = execution_time(start_time)
        total += ex_time
        result2 = f'{len(result):9} {total // n: 5d}'
    print(result2, end='')

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.three_sum_copy_dict(nums)
        ex_time = execution_time(start_time)
        total += ex_time
        result2 = f'{len(result):9} {total // n: 5d}'
    print(result2, end='')

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.three_sum_no_copy_dict(nums)
        ex_time = execution_time(start_time)
        total += ex_time
        result2 = f'{len(result):9} {total // n: 5d}'
    print(result2, end='')

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.three_sum_no_copy_set(nums)
        ex_time = execution_time(start_time)
        total += ex_time
        result3 = f'{len(result):9} {total // n: 5d}'
    print(result3, end='')

    print('\n')
    print(result)


if __name__ == "__main__":
    main()
