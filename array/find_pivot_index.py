'''
Problem:
Given an array of integers nums, calculate the pivot index of this array.

Example:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
left sum = 1 + 7 + 3 = 11, right sum = 5 + 6 = 11.

Approach:
Left Sum = sum(0 to i-1)
Right Sum = sum(i+1 to end)
If Left Sum == Right Sum, pivot found

Brute force:
for i in range(len(nums)):
    lsum=sum(nums[:i])
    rsum=sum(nums[i+1:])
    if lsum==rsum:
        return i
But it gives O(n^2) time complexity.

So, we use prefix sums here.
'''
# @lc app=leetcode id=724 lang=python3
# [724] Find Pivot Index
# @lc code=start
from typing import List

class Solution:
    '''
    Given an array of integers nums, calculate the pivot index of this array.
    '''
    def pivot_index(self, nums: List[int]) -> int:
        '''Calculate the pivot index of this array'''
        total=sum(nums)
        lsum=0
        for i,num in enumerate(nums):
            #total-lsum-num is the right sum
            if lsum==total-lsum-num:
                return i
            lsum+=num
        return -1

# @lc code=end

