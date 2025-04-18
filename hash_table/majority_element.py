'''
Problem:
Given an array nums of size n, return element that appears more than ⌊n / 2⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: 3

Approach: Hashmap
1. Create a hashmap (dict)
2. Iterate over nums, count no of times an element is found
3. Compare each element of hashmap with n//2
4. if hashmap[k]>len(nums)//2, element is k.
'''
from typing import List
# @lc app=leetcode id=169 lang=python3
# [169] Majority Element
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        for k in hashmap:
            if hashmap[k]>len(nums)//2:
                return k    # Return majority *element*, not no of times it was found

# @lc code=end

