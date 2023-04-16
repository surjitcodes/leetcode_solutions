import sys
import time
import random
import json

from collections import Counter


class Solution(object):
    
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:

        # Rename k as carry
        carry = k

        # Process digits of num in the reverse order
        for i in range(len(num) - 1, -1, -1):

            # Add carry to i-th position
            num[i] += carry

            # Extract carry from num[i] for next place
            carry, num[i] = divmod(num[i], 10)

        # Handle the final carry
        if carry:
            num = list(map(int, str(carry))) + num

        # Return the final num
        return num


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
    num = [8, 7, 5]
    k = 9406

    print(num[:20], k)

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.addToArrayForm(num, k)
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
