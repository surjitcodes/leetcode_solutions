import sys
import time
import random
import json

from collections import Counter
from enum import Enum
from itertools import zip_longest

from past.builtins import xrange


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def linked_list_from_list(input_list):
    dummy_head = ListNode(0)
    tail = dummy_head
    for value in input_list:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy_head.next


def list_from_linked_list(head):
    node = head
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


def print_list(head):
    node = head
    print("head", end=' -> ')
    while node is not None:
        print(node.val, end=' -> ')
        node = node.next
    print('None')


class Solution:
    def mergeTwoLists(self, list_1, list_2):

        # Edge case, list_1 is empty
        if list_1 is None:
            return list_2

        # Edge case, list_2 is empty
        if list_2 is None:
            return list_1

        # Recursive case
        if list_1.val <= list_2.val:
            list_1.next = self.mergeTwoLists(list_1.next, list_2)
            return list_1
        else:
            list_2.next = self.mergeTwoLists(list_1, list_2.next)
            return list_2


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
    list1 = linked_list_from_list([1,2,4])
    list2 = linked_list_from_list([1,3,4])
    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.mergeTwoLists(list1, list2)
    print(list_from_linked_list(result))
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
