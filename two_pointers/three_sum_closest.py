'''
Problem:
Given an integer array nums of length n and an integer target
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

Example:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Approach:
i+j+k ~ target
can be lower than target OR greater than target, just as close as possible

1. sort array - so that we can efficiently use 2 pointers
2. closest = float('inf') - to start with a v large number
3. iterate over nums array:
    - l = i+1, r = len(nums)-1 => 3 pointers - i, i+1, last element of array
4. while l < r:
    - current sum = i+nums[l]+nums[r]
    - if current sum is closer to target than previous sum, update closest to current sum:
        - if abs(curr_sum - target) < abs(closest - target), closest = curr_sum # abs because -ve or +ve doesn't matter here
        - if current sum < target, move l towards right, else move r towards left
5. return closest

'''
from typing import List
# @lc app=leetcode id=16 lang=python3
# [16] 3Sum Closest
# @lc code=start
class Solution:
    """find three integers in nums such that the sum is closest to target.
    """
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        """find three integers in nums such that the sum is closest to target.

        Args:
            nums (List[int]): integer array
            target (int): integer to be compared to

        Returns:
            int: sum of three int closest to target
        """
        nums.sort()
        closest=float('inf')
        for i,num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l<r:
                curr_sum = num + nums[l] + nums[r]
                if abs(curr_sum - target) < abs(closest - target):
                    closest=curr_sum
                elif curr_sum < target:
                    l+=1
                else:
                    r-=1
        return closest

# @lc code=end
