import collections
import sys
import time
import random
import json

class Solution:
    def removeStones(self, stones):
        k = 10001

        def find_representative(x):
            if x == rep[x]:
                return x
            # Uses Path compression
            return find_representative(rep[x])

        def perform_union(x, y):
            rx = find_representative(x)
            ry = find_representative(y)
            if rx == ry:
                return False

            if size[rx] < size[ry]:
                rep[rx] = ry
                size[ry] += size[rx]
            else:
                rep[ry] = rx
                size[rx] += size[ry]
            return True  # Two components merged

        rep = [i for i in range(2*k)]
        size = [1 for _ in range(2*k)]
        marked = set()
        for stone in stones:
            marked.add(stone[0])  # Mark x coord
            marked.add(stone[1]+k)  # Mark y coord

        component_count = len(marked)
        for stone in stones:
            x = stone[0]
            y = stone[1] + k
            if perform_union(x, y):
                component_count -= 1

        return len(stones) - component_count


'''
class Solution {
    final int K = 10001;
    // Returns the representative of vertex x
    int find(int[] rep, int x) {
        if (x == rep[x]) {
            return x;
        }
        return rep[x] = find(rep, rep[x]);
    }
    // Combine the stone x and y, and returns 1 if they were not connected
    int performUnion(int [] rep, int [] size, int x, int y) {
        x = find(rep, x);
        y = find(rep, y);
        
        if (x == y) {
            return 0;
        }
        
        if (size[x] > size[y]) {
            rep[y] = x;
            size[x] += size[y];
        } else {
            rep[x] = y;
            size[y] += size[x];
        }
        
        return 1;
    }
    
    public int removeStones(int[][] stones) {
        int[] rep = new int[2 * K + 1];
        int[] size = new int[2 * K + 1];
        // Initialize rep to itself and size as 1
        for (int i = 0; i < 2 * K + 1; i++) {
            rep[i] = i;
            size[i] = 1;
        }
        
        int componentCount = 0;
        HashMap <Integer, Integer> marked = new HashMap<>();
        for (int[] stone : stones) {
            if (!marked.containsKey(stone[0])) {
                componentCount++;
            }
            
            if (!marked.containsKey(stone[1] + K)) {
                componentCount++;
            }
            
            marked.put(stone[0], 1);
            marked.put(stone[1] + K, 1);
        }

        for (int i = 0; i < stones.length; i++) {
            int x = stones[i][0];
            int y = stones[i][1] + K;
            // Decrement the componenets if union invloved merging
            componentCount -= performUnion(rep, size, x, y);
        }
        // Return the maximum stone that can be removed
        return stones.length - componentCount;
    }
};

'''

input = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [3, 3]]
sol = Solution()
result = sol.removeStones(input)
print(result)
