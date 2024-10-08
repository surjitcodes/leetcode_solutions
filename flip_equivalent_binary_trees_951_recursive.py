import collections
import sys
import time
import random
import json


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_tree_root_from_bfs(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = [root]                                  # Leaf nodes of this will not be used

    for i in range(1, len(nums), 2):                # Two children per parent
        parent = queue.pop(0)                       # FIFO processing of nodes. Each parent gets two children
        print("Parent node {}".format(parent.val), end='')

        if nums[i] is not None:                                 # None for no left subtree
            node = TreeNode(nums[i])
            parent.left = node
            queue.append(node)
            print(",  left child is {}".format(node.val), end='')

        if i+1 < len(nums) and nums[i+1] is not None:           # None for no right subtree
            node = TreeNode(nums[i+1])
            parent.right = node
            queue.append(node)
            print(",  right child is {}".format(node.val), end='')
        print()
    return root


def get_tree_nodes_from_bfs(nums):    # Normally only root is needed to be returned. Then use other program
    if not nums:
        return [None]

    root = TreeNode(nums[0])
    nodes_list = [root]
    queue = [root]

    for i in range(1, len(nums), 2):                # Two children per parent
        parent = queue.pop(0)                       # FIFO processing of nodes
        print("Parent node {}".format(parent.val), end='')

        if nums[i] is not None:                                 # None for no left subtree
            node = TreeNode(nums[i])
            nodes_list.append(node)
            parent.left = node
            queue.append(node)
            print(",  left child is {}".format(node.val), end='')

        if i+1 < len(nums) and nums[i+1] is not None:           # None for no right subtree
            node = TreeNode(nums[i+1])
            nodes_list.append(node)
            parent.right = node
            queue.append(node)
            print(",  right child is {}".format(node.val), end='')
        print()
    return nodes_list                   # First node in this list is the root, ie nodes_list[0]


def show_tree_from_nodes(nodes_list):
    for node in nodes_list:
        if not node or not node.left and not node.right:
            continue
        if node.left:
            print("{} - <".format(node.left.val), end='')
        else:
            print("     ", end='')
        print("({})".format(node.val), end='')
        if node.right:
            print("> - {}".format(node.right.val), end='')
        print()


def show_tree_from_root(root):              # preorder traversal
    if not root or not root.left and not root.right:
        return
    if root.left:
        print("{} --- ".format(root.left.val), end='')
    else:
        print("      ", end='')
    print(":{}:".format(root.val), end='')
    if root.right:
        print(" --- {}".format(root.right.val), end='')
    print()
    show_tree_from_root(root.left)
    show_tree_from_root(root.right)


def bfs_traversal(root):                          # Breadth First search of a tree
    output = []
    queue = [root]
    while queue:
        node = queue.pop(0)             # FIFO processing of nodes
        if node:
            output.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:                           # To get list in the input form
            output.append(None)         # We can skip this and next two statements

    while output and not output[-1]:    # remove trailing None values - optional
        output.pop()

    return output


def preorder_traversal(root):

    def preorder(node):
        if node:
            output.append(node.val)
            preorder(node.left)
            preorder(node.right)

    output = []
    preorder(root)
    return output


def inorder_traversal(root):

    def inorder(node):
        if node:
            inorder(node.left)
            output.append(node.val)
            inorder(node.right)

    output = []
    inorder(root)
    return output


def postorder_traversal(root):

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            output.append(node.val)

    output = []
    postorder(root)
    return output


class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))


root1 = [1,2,3,4,5,6,None,None,None,7,8]
root2 = [1,3,2,None,6,4,5,None,None,None,None,8,7]
root1 = get_tree_root_from_bfs(root1)
root2 = get_tree_root_from_bfs(root2)

sol = Solution()
result = sol.flipEquiv(root1, root2)
print(result)
