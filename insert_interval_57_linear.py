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
        """
        #def overlap(a, b):
            #return min(a[1], b[1]) - max(a[0], b[0]) >= 0
        """
        def merge_intervals(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        print(intervals, new_interval)

        if not intervals:
            return [new_interval]

        if new_interval[1] < intervals[0][0]:
            return [new_interval] + intervals

        pos = 0

        merged = []

        while pos < len(intervals):
            if overlap(intervals[pos], new_interval):
                break
            else:
                pos += 1

        if pos == len(intervals):
            return intervals + [new_interval]

        print(pos, merged)

        merged = merged + intervals[:pos]
        merged.append(merge_intervals(intervals[pos], new_interval))
        pos += 1

        while pos < len(intervals):
            if merged[-1][1] >= intervals[pos][0]:
                merged[-1][1] = max(merged[-1][1], intervals[pos][1])
                pos += 1
            else:
                break

        print(pos, merged)

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
        bool isIntervalInserted = false;
        for (int i = 0; i < intervals.size(); i++) {
            if (newInterval[0] < intervals[i][0]) {
                // Found the position, insert the interval and break from the loop.
                intervals.insert(intervals.begin() + i, newInterval);
                isIntervalInserted = true;
                break;
            }
        }
        
        // If there is no interval with a greater value of start value,
        // then the interval must be inserted at the end of the list.
        if (!isIntervalInserted) {
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
b = [0, 1]
sol = Solution()
result = sol.insertInterval(a, b)
print(result)
