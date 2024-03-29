import sys
import time
import random
import json


class Solution:
    def two_sum_brute(self, nums: list[int], target: int) -> list[int]:
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
        return [-1, -1]

    def two_sum_hash(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        hash_map = {}
        
        for i in range(n):
            complement = target - nums[i]
            
            if complement in hash_map:
                return [hash_map[complement], i]
            
            else:
                hash_map[nums[i]] = i
                
        return [-1, -1]

    def two_sum_pointer(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            total = nums[low] + nums[high]
            if total == target:
                return [low, high]
            elif total < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]

    def two_sum_pointer_new(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        low = 0
        high = n - 1
        low_fast = high_fast = True
        while low < high:
            total = nums[low] + nums[high]
            if total == target:
                return [low, high]
            elif total < target:  # increase low
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
        return [-1, -1]


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
        json_data.sort()
    return json_data


def main():
    nums = read_rand_list()
    limits = [(3, 997), (221, 400), (221, 995), (201, 601), (900, 930), (997, 998), (1, 8)]
    print(nums[:15], '\n', nums[len(nums) - 15:])
    print(" low  high target             Brute                 Hash              Two Pointer        Two Pointer New")
    for limit in limits:
        target = nums[limit[0]] + nums[limit[1]]
        print(f"{limit[0]: 4d}  {limit[1]: 4d} {target:6}", end="     ")

        obj_solution = Solution()

        start_time = time.time()
        result_brute = '{}    '.format(obj_solution.two_sum_brute(nums, target))
        result_brute = f'{result_brute[:10]} {execution_time(start_time): 6d}'

        start_time = time.time()
        result_hash = '{}    '.format(obj_solution.two_sum_hash(nums, target))
        result_hash = f'{result_hash[:10]} {execution_time(start_time): 6d}'

        start_time = time.time()
        result_two_pointer = '{}    '.format(obj_solution.two_sum_pointer(nums, target))
        result_two_pointer = f'{result_two_pointer[:10]} {execution_time(start_time): 6d}'

        start_time = time.time()
        result_two_pointer_new = '{}    '.format(obj_solution.two_sum_pointer_new(nums, target))
        result_two_pointer_new = f'{result_two_pointer_new[:10]} {execution_time(start_time): 6d}'

        print(result_brute, end="     ")
        print(result_hash, end="     ")
        print(result_two_pointer, end="     ")
        print(result_two_pointer_new)
    

if __name__ == "__main__":
    main()
