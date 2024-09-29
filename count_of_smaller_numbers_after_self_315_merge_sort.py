import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        print(nums)
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]
        result = [0] * n

        def merge_sort(left, right):
            # print(left, right, arr)
            # merge sort [left, right) from small to large, in place
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)
            merge(left, right, mid)

        def merge(left, right, mid):
            print(left, right, mid, arr, result)
            # merge [left, mid) and [mid, right)
            i = left  # current index for the left array
            j = mid  # current index for the right array
            # use temp to temporarily store sorted array
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    # j - mid numbers jump to the left side of arr[i]
                    result[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            # when one of the subarrays is empty
            while i < mid:
                # j - mid numbers jump to the left side of arr[i]
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            # restore from temp
            for i in range(left, right):
                arr[i] = temp[i - left]
            print(left, right, mid, arr, result, "\n")

        merge_sort(0, n)
        print(arr)

        return result


nums = [5, 1, 2, 1, 6, 2, 1]
sol = Solution()
result = sol.countSmaller(nums)
print(result)
