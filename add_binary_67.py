import sys
import time
import random
import json


class Solution:
    def addBinary_bit_by_bit(self, a, b) -> str:
        n = max(len(a), len(b))
        # Equalize the lengths of two strings
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        output = []

        # Process the digits in the reverse order
        for i in range(n - 1, -1, -1):
            # Add i-th bits of a and b to carry
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            # append unit place of carry to result
            if carry % 2 == 1:
                output.append('1')
            else:
                output.append('0')

            # Find carry for the next place
            carry //= 2

        # Append the final carry
        if carry == 1:
            output.append('1')

        # Correct the order of digits
        output.reverse()

        return ''.join(output)

    def addBinary_bit_manipulation(self, a, b) -> str:
        # Convert the numbers to the int form
        int_a, int_b = int(a, 2), int(b, 2)

        # While int_b is not zero
        while int_b:

            # Find bit_sum and bit_carry
            sum_bits = int_a ^ int_b
            carry_bits = (int_a & int_b) << 1

            # copy them to new a_sum and b_sum
            int_a, int_b = sum_bits, carry_bits

        # Return the sum as binary string
        return bin(int_a)[2:]

    def addBinary_bit_manipulation_fast(self, a, b) -> str:
        # Convert the numbers to the int form
        int_a, int_b = int(a, 2), int(b, 2)

        # While int_b is not zero
        while int_b:
            # Find int_a and int_b for next iteration
            int_a, int_b = int_a ^ int_b, (int_a & int_b) << 1

        # Return the sum as binary string
        return bin(int_a)[2:]


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
    str1 = "11101"
    str2 = "1001"

    print(str1[:20], str2[:20])

    n = 1

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.addBinary_bit_by_bit(str1, str2)
        ex_time = execution_time(start_time)
        total += ex_time
        result1 = f'{result} {total // n: 5d}'
    print(result1, end='  ')

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.addBinary_bit_manipulation(str1, str2)
        ex_time = execution_time(start_time)
        total += ex_time
        result1 = f'{result} {total // n: 5d}'
    print(result1, end='  ')

    total = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        result = obj_sol.addBinary_bit_manipulation_fast(str1, str2)
        ex_time = execution_time(start_time)
        total += ex_time
        result1 = f'{result} {total // n: 5d}'
    print(result1, end='  ')

    print('\n')
    # print(result)


if __name__ == "__main__":
    main()
