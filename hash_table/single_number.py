'''
Problem:
Given a non-empty array of integers nums, every x appears twice except for one. Find that single one.

Example:
Input: nums = [4,1,2,1,2]
Output: 4

Approach:
freq mapping, if count[num]==1, return num
This gives TC O(n), SC O(n) (The count dict can grow to size O(n))
But we want constant extra space (O(1))

So, we go with bitwise XOR.
1. set x to 0
2. loop thru nums:
    - x ^ x = 0, x ^ 0 = x, so only element which is unique will be left
'''
from typing import List
# @lc app=leetcode id=136 lang=python3
# [136] Single Number
# @lc code=start

class Solution:
    def single_number(self, nums: List[int]) -> int:
        #freq mapping method -
        # count={}
        # for n in nums:
        #     count[n]=count.get(n,0)+1
        # for c in count:
        #     if count[c]==1:
        #         return c

        #XOR method -
        x = 0 #single element to be found
        for n in nums:
            x = x ^ n
        return x


# @lc code=end

