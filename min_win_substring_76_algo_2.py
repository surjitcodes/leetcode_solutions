import sys
import time
import random
import json
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_count = Counter(t)
        required = len(t_count)
        left, right, formed = 0, 0, 0
        win_count = {}
        out = float("inf"), None, None

        filtered_s = []
        for pos, ch in enumerate(s):
            if ch in t_count:
                filtered_s.append((pos, ch))

        while right < len(filtered_s):
            ch = filtered_s[right][1]
            win_count[ch] = win_count.get(ch, 0) + 1

            if win_count[ch] == t_count[ch]:
                formed += 1

            while left <= right and formed == required:
                start = filtered_s[left][0]
                end = filtered_s[right][0]
                if end - start + 1 < out[0]:
                    out = (end - start + 1, start, end)

                ch = filtered_s[left][1]
                win_count[ch] -= 1
                if win_count[ch] < t_count[ch]:
                    formed -= 1
                left += 1

            right += 1
        return "" if out[0] == float("inf") else s[out[1]: out[2] + 1]

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
    s = "adabecodebaobcd"
    t = "abcb"
    # string = gen_rand_alpha_num(10000)
    print(s[:60], "...  len", len(s))
    print(t[:60], "...  len", len(t))

    print('Brute force         2-pointer')

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.minWindow(s, t)
    time1 = execution_time(start_time)
    output = f'{result}   {time1: 6d}'
    print(output, end='        ')
    print()


if __name__ == "__main__":
    main()
