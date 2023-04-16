import sys
import time
import random
import json


class Solution:
    def maxArea_brute(self, height: list[int]) -> int:

        max_area = 0

        for left in range(len(height)):
            for right in range(left + 1, len(height)):

                min_height = min(height[left], height[right])
                area = min_height * (right - left)

                max_area = max(max_area, area)

                print(f"{left}         {right}          {right-left}        min ({height[left]},  {height[right]}) = {min_height}         {area}           {max_area}")

        return max_area

    def maxArea_2_pointer(self, height: list[int]) -> int:

        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:

            min_height = min(height[left], height[right])
            area = min_height * (right - left)

            max_area = max(max_area, area)

            print(
                f"{left}         {right}          {right - left}        min ({height[left]},  {height[right]}) = {min_height}         {area}           {max_area}")

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


def execution_time(start_time):
    return int((time.time() - start_time) * 1.0e6)
    # return f"{method} {(time.time() - start_time) * 1.0e6:.03f}"


def gen_rand_alpha_num(count):
    ss = ''
    for i in range(count):
        x = random.randint(0, 35)
        if x < 10:
            s = str(x)
        else:
            s = chr(x+87)
        ss += s
    return ss


def read_rand_list() -> int:
    with open('random_data.json') as json_file:
        json_data = json.load(json_file)
        #  json_data.sort()
    return json_data


def main():
    height = [2, 1, 4, 7, 8, 4]
    # string = gen_rand_alpha_num(10000)
    print(height[:60], "...  len", len(height))

    print('Brute force         2-pointer')

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.maxArea_brute(height)
    time1 = execution_time(start_time)
    output = f'{result}   {time1: 6d}'
    print(output, end='        ')
    print()

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.maxArea_2_pointer(height)
    time1 = execution_time(start_time)
    output = f'{result}   {time1: 6d}'
    print(output, end='        ')

    print()


if __name__ == "__main__":
    main()
