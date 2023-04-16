import sys
import time
import random
import json

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        chars = {}

        left = 0
        for right in range(len(s)):
            if s[right] in chars:
                left = max(chars[s[right]], left)

            result = max(result, right - left + 1)
            chars[s[right]] = right + 1

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
