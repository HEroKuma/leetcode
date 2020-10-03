# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#
#  
# Example 1:
#
#
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
#
#
# Example 2:
#
#
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
#
# Example 3:
#
#
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
#
# Example 4:
#
#
# Input: n = 2
# Output: true
# Explanation: The binary representation of 10 is: 1010.
#
# Example 5:
#
#
# Input: n = 3
# Output: false
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 231 - 1
#
#


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        c = 0
        while n > 0:
            c = n%2
            n = n//2
            if c == n%2:
                return False
        return True
