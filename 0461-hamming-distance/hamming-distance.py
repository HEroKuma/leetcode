# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
#
#


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = "{0:031b}".format(x)
        y = "{0:031b}".format(y)
        c = 0
        for i in range(0, 31):
            if int(x[i]) ^ int(y[i]) is 1:
                c += 1
        return c
