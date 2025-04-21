'''
Problem:
Write an algorithm to determine if a number n is happy:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
3. Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1 => return True

Approach:
Brute Force:
till we don't hit 1:    # while n!=1
    - keep looping over sum of squares  # sum(int(digit)**2 for digit in str(n))
    - store each sum of squares in set  # visited.add(n)
    - if hit 1, return True # (if out of while loop, return True)
    - if sum found in set, return False # if n in visited, return False

Optimised: Floyd's Tortoise and Hare algorithm
'''

# @lc app=leetcode id=202 lang=python3
# [202] Happy Number
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        while n!=1:
            if n in visited:
                return False
            visited.add(n)
            n=sum(int(digit)**2 for digit in str(n))
        return True

# @lc code=end

