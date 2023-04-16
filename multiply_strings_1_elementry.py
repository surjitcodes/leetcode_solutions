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

        products = []
        # For each digit in second, multiply the digit by first
        for index, digit in enumerate(second):
            products.append(self.get_product(index, digit, first))

        # Add all of the results, to get final answer (in reverse order)
        print(products)
        result = self.add_products(products)

        # Reverse answer and join the digits to get the final answer.
        return ''.join(str(digit) for digit in reversed(result))

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

    def add_products(self, products: list[list[int]]) -> list[int]:
        total = products.pop()  # First product is initial total.

        # Add each product to total one at a time.
        for product in products:
            carry, new_total = 0, []

            # Sum each digit from total and product.
            for d1, d2 in zip_longest(total, product, fillvalue=0):
                # Add current digits from both product and total.
                sum_of_digits = d1 + d2 + carry
                carry = sum_of_digits // 10           # New carry
                new_total.append(sum_of_digits % 10)  # Remainder

            if carry != 0:
                new_total.append(carry)

            total = new_total          # Update total

        return total


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
    num2 = "467"

    print(num1[:20], num2[:20])

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.multiply(num1, num2)
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
