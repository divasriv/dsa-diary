'''
Problem:
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]

Example 2:
Input: digits = [9]
Output: [1,0]

Brute Force Approach:
convert to string, then to int, then add 1, then convert to list.
Time complexity: O(n), but Space complexity: O(n) too, it creates a new list.

Optimized Approach:
1. Start from the last digit
2. if digit < 9, add 1
3. if digit == 9, set it to 0 and carry over 1 to the next digit.
4. If all digits are 9, add 1 at the beginning of the list.
'''
from typing import List
# @lc app=leetcode id=66 lang=python3
# [66] Plus One
# @lc code=start
class Solution:
    '''
    Given a non-empty array of digits representing a non-negative integer,
    increment one to the integer.
    '''
    def plus_one(self, digits: List[int]) -> List[int]:
        '''Increment one to the integer represented by digits'''
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:  # digits[i] < 9
                digits[i] += 1
                return digits
        return [1] + digits #will reach here only if all digits are 9
                          #so we need to add 1 at the beginning.
# @lc code=end
