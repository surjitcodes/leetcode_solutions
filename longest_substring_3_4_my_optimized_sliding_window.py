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

    def my_lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        char_pos = {}

        win_closed = -1
        for win_open in range(len(s)):
            if s[win_open] in char_pos:
                win_closed = max(char_pos[s[win_open]], win_closed)

            result = max(result, win_open - win_closed)
            char_pos[s[win_open]] = win_open
            # print(f'{win_closed}  {win_open}  {result}  {s[win_closed+1: win_open+1]}  {chars}')

        return result


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
    string = "abcdaeacf"
    string = gen_rand_alpha_num(10000)
    print(string[:60], "...  len", len(string))

    print('Optimized         my optimised     Improvement')

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.lengthOfLongestSubstring(string)
    time1 = execution_time(start_time)
    output = f'{result}   {time1: 6d}'
    print(output, end='        ')

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.my_lengthOfLongestSubstring(string)
    time2 = execution_time(start_time)
    output = f'{result}   {time2: 6d}'
    print(output, end='     ')
    print(f'{(time1-time2)*100/time1:.02f}%')


if __name__ == "__main__":
    main()
