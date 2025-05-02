'''
Problem:
Given an array of intervals where intervals[i] = [start, end]
merge all overlapping intervals
return an array of the non-overlapping intervals

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]  # 2 is within [1,3], so 1,2,3,6 -> [1,6]

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping

Approach:
Brute force:
sort intervals
start from the first interval and compare it with all other intervals
If the first interval overlaps with any other interval:
    - remove the other interval from the list
    - merge into first interval
Repeat for remaining intervals

Optimized:
Sort based on the starting points
Traverse intervals, starting from first interval:
    - if curr interval != first interval
        - if overlap with prev interval, merge with prev interval
        - if no overlap, move to next inteval
'''
from typing import List
# @lc app=leetcode id=56 lang=python3
# [56] Merge Intervals
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Brute Force
        # intervals.sort()
        # result=[]
        # for i in range(len(intervals)):
        #     start=intervals[i][0]
        #     end=intervals[i][1]
        #     if result and result[-1][1] >= end: # if last element of last array in element >= end
        #         continue
        #     for j in range(i + 1, len(intervals)):
        #         if intervals[j][0] <= end:
        #             end = max(end,intervals[j][1])
        #     result.append([start,end])
        # return result

        # Optimized
        intervals.sort()
        index = 0 # index of prev interval
        for i in range(1, len(intervals)):
            # if curr interval overalps with prev interval
            if intervals[index][1]>=intervals[i][0]:
                intervals[index][1]=max(intervals[index][1],intervals[i][1])
            else:
                index+=1
                intervals[index]=intervals[i]
        return intervals[:index + 1]


# @lc code=end
s=Solution()
# print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[7, 8], [1, 5], [2, 4], [4, 6]]))
