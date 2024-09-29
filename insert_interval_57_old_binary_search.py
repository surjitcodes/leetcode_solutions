import collections
import itertools
import sys
import time
import random
import json


class Solution:
    def insertInterval(self, intervals, new_interval):

        def overlap(a, b):
            return a[0] <= b[1] and b[0] <= a[1]

        def merge_intervals(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        print(intervals, new_interval)
        if not intervals:
            return [new_interval]
        if new_interval[1] < intervals[0][0]:
            return [new_interval] + intervals
        if intervals[-1][1] < new_interval[0]:
            return intervals + [new_interval]

        left, right = 0, len(intervals) - 1
        print(left, right, (left + right) // 2)

        while left < right:
            mid = (left + right) // 2
            if new_interval[0] <= intervals[mid][0]:
                right = mid
            else:
                left = mid + 1
            print(left, right, mid)

        pos = left
        print(pos)

        if pos > 0 and overlap(intervals[pos-1], new_interval):
            print("previous also merging")
            pos -= 1

        merged = intervals[:pos] if pos > 0 else []
        print(merged)
        merged.append(merge_intervals(intervals[pos], new_interval))
        pos += 1

        while pos < len(intervals):
            if merged[-1][1] >= intervals[pos][0]:
                merged[-1][1] = max(merged[-1][1], intervals[pos][1])
                pos += 1
            else:
                break

        # print(pos, merged)

        return merged + intervals[pos:]


"""
class Solution {
public:
    // Returns true if the intervals a and b have a common element.
    bool doesIntervalsOverlap(vector<int>& a, vector<int>& b) {
        return min(a[1], b[1]) - max(a[0], b[0]) >= 0;
    }
    
    // Return the interval having all the elements of intervals a and b.
    vector<int> mergeIntervals(vector<int>& a, vector<int>& b) {
        return {min(a[0], b[0]), max(a[1], b[1])};
    }

    // Insert the interval newInterval, into the list interval keeping the sorting order intact.
    void insertInterval(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int index = upper_bound(intervals.begin(), intervals.end(), newInterval) - intervals.begin();
        
        if (index != intervals.size()) {
            intervals.insert(intervals.begin() + index, newInterval);
        } else {
            intervals.push_back(newInterval);
        }
    }
    
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        // Insert the interval first before merge processing.
        insertInterval(intervals, newInterval);
        
        vector<vector<int>> answer;
        for (int i = 0; i < intervals.size(); i++) {
            vector<int> currInterval = {intervals[i][0], intervals[i][1]};
            // Merge until the list gets exhausted or no overlap is found.
            while (i < intervals.size() && doesIntervalsOverlap(currInterval, intervals[i])) {
                currInterval = mergeIntervals(currInterval, intervals[i]);
                i++;
            }
            // Decrement to ensure we don't skip the interval due to outer for-loop incrementing.
            i--;
            answer.push_back(currInterval);
        }
        
        return answer;
    }
};

"""
a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
b = [5, 6]
sol = Solution()
result = sol.insertInterval(a, b)
print(result)
