# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
#
#
# Example 1:
#
#
# Input: "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: "ZY"
# Output: 701
#


class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i, j in enumerate(s[::-1]):
            base = ord(j) - ord('A') + 1
            # print(base)
            ans += base*(26**i)
        return ans
