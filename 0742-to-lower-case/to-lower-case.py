# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#
#  
#
#
# Example 1:
#
#
# Input: "Hello"
# Output: "hello"
#
#
#
# Example 2:
#
#
# Input: "here"
# Output: "here"
#
#
#
# Example 3:
#
#
# Input: "LOVELY"
# Output: "lovely"
#
#
#
#


class Solution:
    def toLowerCase(self, string: str) -> str:
        ans = ''
        for i in string:
            if 'A' <= i <= 'Z':
                ans += chr(ord(i)-ord('A')+ord('a'))
            else:
                ans += i
        return ans
