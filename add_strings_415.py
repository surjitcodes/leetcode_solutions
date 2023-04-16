import sys
import time
import random
import json


class Solution:
    def addStrings(self, str1: str, str2: str) -> str:
        carry, output = 0, []

        pos1, pos2 = len(str1) - 1, len(str2) - 1   # Get unit places

        while pos1 >= 0 or pos2 >= 0:    # Continue if digit is present
            total = carry

            # Add the digits to total
            if pos1 >= 0:
                total += ord(str1[pos1]) - ord('0')
            if pos2 >= 0:
                total += ord(str2[pos2]) - ord('0')

            output.append(total % 10)   # Append unit place to output
            carry = total // 10         # Find carry for next position

            # Move the two pointers
            pos1 -= 1
            pos2 -= 1

        if carry:                     # Handle the final carry
            output.append(carry)

        return ''.join(str(i) for i in output[::-1])
    
    
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
    str1 = "9546"
    str2 = "627"

    print(str1[:20], str2[:20])
    print(ord('0'))
    n = 1

    total = 0
    output = 0
    for i in range(n):
        start_time = time.time()
        obj_sol = Solution()
        output = obj_sol.addStrings(str1, str2)
        ex_time = execution_time(start_time)
        total += ex_time
        output = f'{output} {total // n: 5d}'
    print(output, end='  ')

    print('\n')
    # print(outputult)


if __name__ == "__main__":
    main()
