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
    def addTwoNumbers(self, x, y) -> ListNode:
        dummy_head = ListNode(0)
        node = dummy_head
        carry = 0
        while x or y or carry:
            x_val = x.val if x else 0
            y_val = y.val if y else 0
            column_sum = x_val + y_val + carry
            carry = column_sum // 10
            new_node = ListNode(column_sum % 10)
            node.next = new_node
            node = new_node
            x = x.next if x else None
            y = y.next if y else None
        return dummy_head.next


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
    x = linked_list_from_list([2,3,4])
    y = linked_list_from_list([4,5,6])
    start_time = time.time()
    print(list_from_linked_list(x))
    print(list_from_linked_list(y))
    obj_sol = Solution()
    result = obj_sol.addTwoNumbers(x, y)
    print(list_from_linked_list(result))
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)


if __name__ == "__main__":
    main()
