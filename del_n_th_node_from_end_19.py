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
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        length -= n
        parent = dummy
        while length > 0:
            length -= 1
            parent = parent.next

        parent.next = parent.next.next
        return dummy.next


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
    x = linked_list_from_list([1,2,3,4,5])
    start_time = time.time()
    print(list_from_linked_list(x))
    obj_sol = Solution()
    result = obj_sol.removeNthFromEnd(x, 2)
    print(list_from_linked_list(result))
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
