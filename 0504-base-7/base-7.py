# Given an integer, return its base 7 string representation.
#
# Example 1:
#
# Input: 100
# Output: "202"
#
#
#
# Example 2:
#
# Input: -7
# Output: "-10"
#
#
#
# Note:
# The input will be in range of [-1e7, 1e7].
#


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = []
        neg = True if num < 0 else False
        num = abs(num)
        while num > 0:
            ans.insert(0, str(num%7))
            num = num//7
        if neg:
            ans.insert(0, '-')
            
        return ''.join(ans)
