# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
#
# Example 1:
#
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#
#
#  
#
# Note:
#
#
# 	S string length is in [1, 10000].
# 	C is a single character, and guaranteed to be in string S.
# 	All letters in S and C are lowercase.
#
#


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        ans, pos = [], -n 
        for i in range(n):
            if S[i] == C:
                pos = i
            ans.append(i-pos)
        print(ans)
        for i in range(n-1,-1,-1):
            if S[i] == C:
                pos = i
            ans[i] = min(ans[i], abs(i-pos))
        return ans
