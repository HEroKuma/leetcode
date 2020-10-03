# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
#  
#
# Note: You may assume the string contains only lowercase English letters.
#


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1
