# Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.
#
# Since the answer may not fit in an integer data type, return the answer as a string.
#
# If there is no answer return an empty string.
#
#  
# Example 1:
#
#
# Input: digits = [8,1,9]
# Output: "981"
#
#
# Example 2:
#
#
# Input: digits = [8,6,7,1,0]
# Output: "8760"
#
#
# Example 3:
#
#
# Input: digits = [1]
# Output: ""
#
#
# Example 4:
#
#
# Input: digits = [0,0,0,0,0,0]
# Output: "0"
#
#
#  
# Constraints:
#
#
# 	1 <= digits.length <= 10^4
# 	0 <= digits[i] <= 9
# 	The returning answer must not contain unnecessary leading zeros.
#
#


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        list0 = sorted([d for d in digits if d%3==0])
        list1 = sorted([d for d in digits if d%3==1])
        list2 = sorted([d for d in digits if d%3==2])
        s = (len(list1) + len(list2)*2)%3
        
        if s==1:
            if list1:
                list1=list1[1:]
            elif len(list2)>=2:
                list2=list2[2:]
            else:
                raise Exception("check logic")
        elif s==2:
            if list2:
                list2=list2[1:]
            elif len(list1)>=2:
                list1=list1[2:]
            else:
                raise Exception("check logic")
        #print(list0, list1, list2)
        final = sorted(list0+list1+list2, reverse=True)
        
        if final and final[0]==0:
            return "0"
        
        return "".join(str(n) for n in final)
