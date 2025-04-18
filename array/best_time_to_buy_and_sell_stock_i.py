'''
Problem:
Array prices, prices[i] is the price of a given stock on the ith day.
e.g. [7,1,5,3,6,4] -> stock price was 7 on day 1, 1 on day 2, etc
Choose a single day to buy, choose a different day to sell
Return the maximum profit you can achieve

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: stock prices only keep decreasing after day1, so if we buy, we don't get any profits, so profit=0

Brute force Approach:
set max_profit to 0
loop thru every day (every day can be a buy day, i)
for each i, loop thru future days, calculate profit (profit = j-i)
compare with max_profit, update it

max_profit=0
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        profit=prices[j]-prices[i]
        max_profit=max(profit, max_profit)
return max_profit

But this gives TC O(n**2)

Optimised approach:
1. Set min_price to inf, set max_profit to 0
2. Loop through prices arr:
    For each price, check if it's lower than the min_price.
        If yes, update min_price.
    Calculate profit: price - min price, compare with max profit:
    If profit is higher than max_profit, update max_profit.
3. After finishing loop, return max_profit
TC: O(n)

'''
from typing import List
# @lc app=leetcode id=121 lang=python3
# [121] Best Time to Buy and Sell Stock
# @lc code=start

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=0
        for price in prices:
            profit=price-min_price
            if price < min_price:
                min_price = price  # Update the lowest price encountered
            elif profit > max_profit:
                max_profit = profit  # Update the maximum profit
        return max_profit

# @lc code=end

