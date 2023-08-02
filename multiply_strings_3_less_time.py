import sys
import time
import random
import json

from collections import Counter
from itertools import zip_longest

from past.builtins import xrange


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result as a string of zeros of length N.
        result = [0] * (len(num1) + len(num2))

        first = num1[::-1]   # Reverse num1 and num2
        second = num2[::-1]

        # Iterate over all pairs of digits of strings
        for index2, digit2 in enumerate(second):
            for index1, digit1 in enumerate(first):

                # Find position where result is to be added
                pos = index1 + index2

                # Digit already present at pos is carry
                val = int(digit1) * int(digit2) + result[pos]

                # Update result after carry adjustment
                result[pos] = val % 10
                result[pos + 1] += val // 10

        # Pop the excess 0 from the end of result.
        if result[-1] == 0:
            result.pop()

        return ''.join(str(digit) for digit in reversed(result))


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
    num1 = "389"
    num2 = "167"

    print(num1[:20], num2[:20])

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.multiply(num1, num2)
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
