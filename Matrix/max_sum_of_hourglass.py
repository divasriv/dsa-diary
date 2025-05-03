'''
Problem:
given an m x n integer matrix grid
this is an hourglass:

a b c
  d
e f g

Return the maximum sum of the elements of an hourglass

Example:
grid= [[-9, -9, -9,  1, 1, 1],
 [0, -9,  0,  4, 3, 2],
[-9, -9, -9,  1, 2, 3],
[ 0,  0,  8,  6, 6, 0],
[ 0,  0,  0, -2, 0, 0],
[ 0,  0,  1,  2, 4, 0]]
Output: 28
(max ->
0  4  3
   1
8  6  6)

Approach:
1. sum up all hourglass elements:
(i,j),(i,j+1),(i,j+2), (i+1,j+1),(i+2,j), (i+2,j+1),(i+2,j+2)
where i,j is position of a specific element while traversing the 2D matrix.
Here, we can't access a value i+2 if there's no i+2th element (in [-9, -9, -9,  1, 1, 1], we can't have 2nd or 3rd 1 as i ). same with j.
so, we say, iteration range is len(grid)-2 : 0th index to 3rd index.
2. Track max sum = max of current max, current sum
3. Return max
'''
from typing import List

# @lc app=leetcode id=2428 lang=python3
# [2428] Maximum Sum of an Hourglass
# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        sum_hourglass=float('-inf')
        max_sum=float('-inf')
        for i in range(len(grid)-2):
            for j in range(len(grid[i])-2):
                sum_hourglass = grid[i][j]+grid[i][j+1]+grid[i][j+2] \
                        + grid[i+1][j+1]                \
                        + grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                # print(f'sum[{[i]}][{[j]}]= {sum_hourglass}')
                max_sum=max(max_sum,sum_hourglass)
        return max_sum

# @lc code=end

