# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
#  
# Example 1:
#
#
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
#
#
# Example 2:
#
#
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
#
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 1000
# 	1 <= arr[i] <= 1000
#
#


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        arr = [s % 2 for s in arr]
        c = 0
        for i in range(1, len(arr)):
            if arr[i] != 0:
                arr[i] += arr[i-1]
        print(arr)
        
        return 3 in arr
