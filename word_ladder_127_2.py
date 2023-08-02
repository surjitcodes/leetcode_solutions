import collections
import sys
import time
import random
import json

from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.length = 0
        # Setting up of graph of one letter change words
        self.generic_dict = defaultdict(list)

    def visit_node(self, queue, visited, others_visited):
        queue_size = len(queue)
        for _ in range(queue_size):
            current_word = queue.popleft()
            for i in range(self.length):
                # Intermediate words for current word
                generic_word = current_word[:i] + "-" + current_word[i + 1:]

                # Next states are all words which share same generic word
                for word in self.generic_dict[generic_word]:
                    # Generic word in both traversals means solution found
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        # Value of dictionary, is the number of hops.
                        visited[word] = visited[current_word] + 1
                        queue.append(word)
        return None

    def ladderLength(self, begin_word, end_word, word_list):
        self.length = len(begin_word)
        if not self.length or end_word not in word_list:
            return 0

        for word in word_list:
            for i in range(self.length):
                # Key is generic word. Value is list of words
                self.generic_dict[word[:i] + "-" + word[i + 1:]].append(word)

        queue_begin = collections.deque([begin_word])  # BFS from begin_word
        queue_end = collections.deque([end_word])  # BFS from end_word
        # Visited to make sure we don't repeat processing same word
        visited_begin = {begin_word: 1}
        visited_end = {end_word: 1}
        ans = None
        while queue_begin and queue_end:
            # Progress forward one step from the shorter queue
            if len(queue_begin) <= len(queue_end):
                ans = self.visit_node(queue_begin, visited_begin, visited_end)
            else:
                ans = self.visit_node(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0


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
