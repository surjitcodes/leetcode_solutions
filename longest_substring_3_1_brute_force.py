import sys
import time
import random
import json


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def acceptable(start, end):
            chars_used = set()

            for i in range(start, end + 1):
                c = s[i]
                if c in chars_used:
                    return False

                chars_used.add(c)

            return True

        n = len(s)
        result = 0

        # Find all the substrings to find the best result
        for i in range(n):
            for j in range(i, n):

                if acceptable(i, j):
                    # Compare result with  len of substring
                    result = max(result, j - i + 1)

        return result


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
    string = "abcdaeacf"

    print(string[:20])

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.lengthOfLongestSubstring(string)
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
