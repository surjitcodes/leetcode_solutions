import sys
import time
import random
import json


class Solution:
    def two_sum_bruteforce(self, nums: list[int], target: int) -> list[int]:
        """
        : type nums: List[int]
        : type target: int
        :rtype: :ist[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                total = nums[i] + nums[j]
                # print(nums[i], nums[j], total)
                if total == target:
                    return [i, j]
        return []

    def two_sum_hash(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        hash_map = {}
        
        for i in range(n):
            complement = target - nums[i]
            
            if complement in hash_map:
                return [hash_map[complement], i]
            
            else:
                hash_map[nums[i]] = i
                
        return []

    def two_sum_sorted(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            total = nums[low] + nums[high]
            if total == target:
                return [low+1, high+1]
            elif total < target:
                low += 1
            else:
                high -= 1
        return [0, 0]

    def two_sum_sorted_new(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        low = 0
        high = n - 1
        low_fast = high_fast = True
        while low < high:
            total = nums[low] + nums[high]
            if total == target:
                return [low+1, high+1]
            elif total < target: # increase low
                low += 1
                if low_fast:
                    mid_old, mid = high, (low+high)//2
                    while mid != mid_old:
                        if nums[mid] + nums[high] < target:
                            low = mid + 1
                        mid_old, mid = mid, (mid + mid_old)//2
                low_fast = False
            else: # decrease high
                high -= 1
                if high_fast:
                    mid_old, mid = low, (low+high)//2
                    while mid != mid_old:
                        if nums[low] + nums[mid] > target:
                            high = mid - 1
                        mid_old, mid = mid, (mid + mid_old)//2
                high_fast = False
        return [0, 0]


def execution_time(start_time, method):
    print(f"{method} execution takes: {(time.time() - start_time) * 1.0e3:.03f} ms")


def gen_save_rand_list(count, limit):
    nums = random.sample(range(1, limit), count)
    with open('random_data.json', 'w') as f:
        json.dump(nums, f)


def read_rand_list() -> int:
    with open('random_data.json') as json_file:
        json_data = json.load(json_file)
        json_data.sort()
        
    print(json_data[:15])
    print(json_data[len(json_data) - 15:])

    return json_data, json_data[42] + json_data[357]


def main():
    nums, target = read_rand_list()
    print(target)

    start_time_hash = time.time()
    obj_solution = Solution()

    result_hash = obj_solution.two_sum_hash(nums, target)
    execution_time(start_time_hash, "hashing")
    print(result_hash)

    start_time_including_sort = time.time()
    nums.sort()
    start_time_presorted = time.time()
    result_sorted = obj_solution.two_sum_sorted(nums, target)
    execution_time(start_time_including_sort, "2 pointer: including sorting")
    execution_time(start_time_presorted, "2 pointer: pre sorted")
    print(result_sorted)

    start_time_including_sort = time.time()
    nums.sort()
    start_time_presorted = time.time()
    result_sorted = obj_solution.two_sum_sorted_new(nums, target)
    execution_time(start_time_including_sort, "2 pointer new: including sorting")
    execution_time(start_time_presorted, "2 pointer new: pre sorted")
    print(result_sorted)
    

if __name__ == "__main__":
    main()
