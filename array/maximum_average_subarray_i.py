'''
Problem:
given an integer array nums consisting of n elements, and an integer k
Find a contiguous subarray with length equal to k, with max avg value,return max avg

Example:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Approach:
Since contiguous subarray is mentioned, it is a sliding window problem
We slide a window of length k over nums array, keep track of the max avg
Initial window: sum of the first k elements - sum(nums[:k])
Take avg of window: max_avg = window_sum / k
Iterate thru nums array starting from k:
    - subtract element sliding out (nums[i-k]), add new element sliding in (nums[i])
    - calculate new avg, compare with current avg, update if new > curr
Return max avg

'''
from typing import List
# @lc app=leetcode id=643 lang=python3
# [643] Maximum Average Subarray I
# @lc code=start
class Solution:
    """find max avg
    """
    def find_max_average(self, nums: List[int], k: int) -> float:
        """find max avg

        Args:
            nums (List[int]): int array
            k (int): subarray length

        Returns:
            float: avg of subarray
        """
        window_sum = sum(nums[:k])
        max_avg = window_sum / k
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, window_sum / k)
        return max_avg

# @lc code=end
