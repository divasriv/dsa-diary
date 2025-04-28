'''
Problem:
Given an integer array nums, find the subarray with the largest product, return product.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6   #2x3=6, 2x3x-2=-12, 2x3x-2x4=-48, 3x-2=-6, 3x-2x4=-24, -2x4=-8 => 6 is max
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0   # -2x0=0, -2x0x-1=0, 0x-1=0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

This is a sliding window problem.
need to track both min and max, cuz -ve x -ve can become +ve big number, -ve/+ve  x 0 = 0

Approach:
set min,max,result as first element
iterate over nums array:
    - store temp_min as min in (current elem, num * max found so far, num * min found so far)
    - same with temp max.. store max of all 3
    - swap into min_prod, max prod (to maintain and update max/min found so far values)
    - result will be max of current result
return once exited from loop

'''
from typing import List
# @lc app=leetcode id=152 lang=python3
# [152] Maximum Product Subarray
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = max_prod = res = nums[0]
        for num in nums[1:]:
            temp_min = min(num, num * max_prod, num * min_prod)
            temp_max = max(num, num * max_prod, num * min_prod)
            min_prod,max_prod = temp_min,temp_max
            res = max(res,max_prod)
        return res

# @lc code=end

s=Solution()
print(s.maxProduct([-2, 3, -4]))
