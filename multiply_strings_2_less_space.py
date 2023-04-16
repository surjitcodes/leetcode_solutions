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

        # Reverse both numbers.
        first = num1[::-1]
        second = num2[::-1]

        # Create space for result.
        result = [0] * (len(first) + len(second))

        # Iterate over all digits in second string
        for index, digit in enumerate(second):
            # Find product of digit with first string
            product = self.get_product(index, digit, first)
            # Add product to the result
            result = self.addStrings(product, result)

        # Pop excess zero from the end of result (if any).
        if result[-1] == 0:
            result.pop()

        # Join the characters in the reverse order.
        return ''.join(str(d) for d in reversed(result))

    def get_product(self, index: int, d2: str, first: str) -> list[int]:
        # Insert zeros at the beginning of line
        carry = 0
        product = [0] * index

        # Multiply each digit in first with d2
        for d1 in first:
            multiplication = int(d1) * int(d2) + carry

            # Set carry equal to the tens place digit of multiplication.
            carry = multiplication // 10

            # Append last digit to the current result.
            product.append(multiplication % 10)

        if carry != 0:
            product.append(carry)
        return product

    def addStrings(self, product: list, result: list) -> list:
        carry = 0
        new_result = []
        for d1, d2 in zip_longest(product, result, fillvalue=0):
            # Add current digits of both numbers.
            sum_of_digits = d1 + d2 + carry
            carry = sum_of_digits // 10
            # Append last digit of curr_sum to the result.
            new_result.append(sum_of_digits % 10)

        return new_result


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
    num1 = "384"
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
