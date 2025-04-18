'''
Problem:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

This is a sliding window problem.
'''
from typing import List
# @lc app=leetcode id=53 lang=python3
# [53] Maximum Subarray
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=curr_sum=nums[0]
        for num in nums[1:]:
            curr_sum = num if curr_sum < 0 else curr_sum + num
            maxsum = max(maxsum, curr_sum)
        return maxsum

# @lc code=end
