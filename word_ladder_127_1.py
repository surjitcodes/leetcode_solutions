import collections
import sys
import time
import random
import json


from collections import defaultdict
class Solution(object):
    def ladderLength(self, begin_word, end_word, word_list):
        L = len(begin_word)  # All words are of same length.

        if not L or end_word not in word_list:
            return 0

        # Setting up of graph of one letter change words
        generic_dict = defaultdict(list)
        for word in word_list:
            for i in range(L):
                # Key is generic word. Value is list of words
                generic_dict[word[:i] + "-" + word[i+1:]].append(word)

        visited = [begin_word]  # To avoid repetition
        queue = collections.deque([(begin_word, 1)])  # Queue for BFS
        while queue:
            current_word, level = queue.popleft()  # BFS
            for i in range(L):
                generic_word = current_word[:i] + "-" + current_word[i+1:]

                # Next level - All words which share the same generic word.
                for word in generic_dict[generic_word]:
                    if word == end_word:  # Found
                        return level + 1
                    if word not in visited:
                        visited.append(word)  # Mark as visited
                        queue.append((word, level + 1))

                generic_dict[generic_word] = []

        return 0  # Solution not found

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
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(begin_word, end_word, word_list)

    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.ladderLength(begin_word, end_word, word_list)
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
