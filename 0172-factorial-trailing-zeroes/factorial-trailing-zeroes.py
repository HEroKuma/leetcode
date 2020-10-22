# Given an integer n, return the number of trailing zeroes in n!.
#
# Follow up: Could you write a solution that works in logarithmic time complexity?
#
#  
# Example 1:
#
#
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
#
# Example 2:
#
#
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
#
# Example 3:
#
#
# Input: n = 0
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 104
#
#


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count2 = 0
        count5 = 0
        for i in range(1, n+1):
            while i % 2 == 0:
                i = i//2
                count2 += 1
            while i % 5 == 0:
                i = i//5
                count5 += 1
        
        return min(count2, count5)
