import sys
import time
import random
import json

from collections import Counter
from enum import Enum
from itertools import zip_longest

from past.builtins import xrange


class Node:
    def __init__(self, value, next, random):
        self.val = value
        self.next = next
        self.random = random


def linked_list_from_list(input_list):
    print(input_list)                   # Input list
    tail = dummy_head = Node(0, None, None)
    node_memory = {}                # Node positions

    # Create nodes, set val and next pointers.
    for pos, info in enumerate(input_list):
        tail.next = Node(info[0], None, None)  # Create node
        tail = tail.next
        node_memory[pos] = tail  # Save memories of all nodes

    # Set random pointers. Iterate over all nodes
    node = head = dummy_head.next
    for info in input_list:
        random_pos = info[1]  # node pos in input
        if random_pos in node_memory:
            node.random = node_memory[random_pos]

        node = node.next

    return head


def list_from_linked_list(head):
    position = {}               # to save node positions
    # Save node positions
    pos = 0
    node = head
    while node:                 # Iterate of all nodes
        position[node] = pos    # save node positions
        node = node.next
        pos += 1

    result = []                 # Output list
    node = head
    pos = 0
    while node:                 # Iterate over all nodes
        if node.random:
            result.append([node.val, position[node.random]])
        else:
            result.append([node.val, None])

        node = node.next
        pos += 1
    return result


def print_list(head):
    node = head
    print("head", end=' -> ')
    while node is not None:
        print(node.val, end=' -> ')
        node = node.next
    print('None')


class Solution(object):
    def __init__(self):
        # Old node is key new node is value
        self.clone_dict = {}

    def get_clone(self, node):
        if not node:            # Node is None
            return None         # Clone is also None

        if node not in self.clone_dict:  # not already cloned
            # Create clone and save it in dictionary
            self.clone_dict[node] = Node(node.val, None, None)

        return self.clone_dict[node]

    def copyRandomList(self, head):
        if not head:
            return head

        node = head  # Process head node
        while node:  # Iterate over all nodes of old list
            # Get clone of node
            clone = self.get_clone(node)
            # Set its pointers
            clone.random = self.get_clone(node.random)
            clone.next = self.get_clone(node.next)

            node = node.next  # Move to next node

        return self.clone_dict[head]


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
    obj = Solution()
    head = linked_list_from_list([[6, 2], [8, None], [4, 1], [9, 0]])
    # print(list_from_linked_list(head))
    result = obj.copyRandomList(head)
    result = list_from_linked_list(result)
    print(result)

    '''
    start_time = time.time()
    obj_sol = Solution()
    result = obj_sol.mergeTwoLists(list1, list2)
    print(list_from_linked_list(result))
    print(result)
    output = f'Count = {result} Time = {execution_time(start_time): 6d}'
    print(output)
    '''


if __name__ == "__main__":
    main()
