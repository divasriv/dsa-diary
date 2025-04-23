'''
Problem:
Convert uppercase to lowercase, remove all non-alphanumeric characters,
Check if phrase reads the same forward and backward

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

My Approach:
two pointer:
remove all non-alpha chars
then s.lower to get string into all lowercase
l,r=0,len(s)-1, check if s[l]=s[r], if yes, l+=1,r-=1
if s[l]!=s[r] at any point, return False

'''
# @lc app=leetcode id=125 lang=python3
# [125] Valid Palindrome
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join([char.lower() for char in s if char.isalnum()])
        l,r=0,len(s)-1
        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
# @lc code=end
sol=Solution()
print(sol.isPalindrome("12321"))
