# Given an integer n, add a dot (".") as the thousands separator and return it in string format.
#
#  
# Example 1:
#
#
# Input: n = 987
# Output: "987"
#
#
# Example 2:
#
#
# Input: n = 1234
# Output: "1.234"
#
#
# Example 3:
#
#
# Input: n = 123456789
# Output: "123.456.789"
#
#
# Example 4:
#
#
# Input: n = 0
# Output: "0"
#
#
#  
# Constraints:
#
#
# 	0 <= n < 2^31
#
#


class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        if n == "0":
            return n
        _list = []
        while n:
            _list.insert(0, n[-3:])
            n = n[:-3]
        print(_list)
            
        return ".".join(_list)
