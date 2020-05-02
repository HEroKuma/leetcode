# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
#
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
#
#
# Note:
# In the string, each word is separated by single space and there will not be any extra space in the string.
#


class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        s = s.split(' ')
        for i in s:
            ans += self.reverse(i)
            ans += ' '
        return ans[:-1]
    
    def reverse(self, s):
        a = ''
        # print(s)
        for i in range(len(s)-1, -1, -1):
            # print(i)
            a += s[i]
        return a
