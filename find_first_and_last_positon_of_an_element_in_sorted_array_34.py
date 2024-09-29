import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def searchRange(self, nums, target) -> list[int]:

        def find_bound(nums, target, first_ocurance: bool) -> int:
            begin, end = 0, len(nums) - 1
            while begin <= end:
                mid = (begin + end) // 2
                if nums[mid] < target:
                    begin = mid + 1
                elif nums[mid] > target:
                    end = mid - 1

                else:       #   nums[mid] == target
                    if first_ocurance:    # Look for lower bound
                        if mid == begin or nums[mid - 1] < target:
                            return mid
                        end = mid - 1  # Search left side

                    else:           # Look for upper bound
                        if mid == end or nums[mid + 1] > target:
                            return mid
                        begin = mid + 1  # Search right side
            return -1

        lower_bound = find_bound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]

        upper_bound = find_bound(nums, target, False)
        return [lower_bound, upper_bound]


nums = [1, 3, 3, 4, 4, 4, 7, 8]
tartet = 4
sol = Solution()
result = sol.searchRange(nums, tartet)
print(result)
