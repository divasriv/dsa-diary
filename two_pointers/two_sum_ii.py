'''
Problem:
Array of integers is sorted in asc order
find 2 nums that add up to target
1 <= index1 < index2 <= numbers.length
Return the indices of the two numbers, index1 and index2, added by one as an integer array of length 2

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Approach:
We are given that output should be 1-based int array.
since input is sorted, we can use 2 pointers
'''
from typing import List
# @lc app=leetcode id=167 lang=python3
# [167] Two Sum II - Input Array Is Sorted
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            curr_sum=numbers[l]+numbers[r]
            if curr_sum==target:
                return [l+1,r+1]
            elif curr_sum>target:
                r-=1
            else:
                l+=1

# @lc code=end
