# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.
#
# Return that integer.
#
#  
# Example 1:
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 10^4
# 	0 <= arr[i] <= 10^5
#


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        something = []
        #arr = [1,2,2,6,6,6,6,7,10]
        uniques = list(set(arr))
        for i in range(0,len(uniques)):
            something.append(arr.count(uniques[i]))
        for i in range(0,len(something)):
            if something[i] > len(arr)/4:
                return uniques[i]
