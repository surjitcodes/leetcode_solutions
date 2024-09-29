import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        def min_number_of_splits(max_sum: int) -> int:
            # to be developed
            split_count = 1
            current_sum = 0

            for element in nums:
                if current_sum + element <= max_sum:
                    current_sum += element
                else:
                    split_count += 1
                    current_sum = element

            print(max_sum, split_count)
            return split_count

        low = max(nums)
        high = sum(nums)

        while low <= high:
            max_sum = (low + high) // 2

            if min_number_of_splits(max_sum) <= k:
                minimum_largest_split_sum = max_sum
                high = max_sum - 1
            else:
                low = max_sum + 1

        return minimum_largest_split_sum


nums = [5, 12, 7, 18, 8]
k = 3
print(nums, k)
sol = Solution()
result = sol.splitArray(nums, k)
print(result)
