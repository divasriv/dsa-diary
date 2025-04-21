'''
Problem:
Given an integer array nums and an integer k, return the k most frequent elements

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Approach:
count frequency of elements in array, store in count dict
sort keys, in reverse, based on frequency
return keys till k
'''
from typing import List
# @lc app=leetcode id=347 lang=python3
# [347] Top K Frequent Elements
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        keys=sorted(count,key=lambda x:count[x],reverse=True)
        return keys[:k]

# @lc code=end

