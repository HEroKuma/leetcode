# Write a program to count the number of days between two dates.
#
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
#
#  
# Example 1:
# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:
# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
#
#  
# Constraints:
#
#
# 	The given dates are valid dates between the years 1971 and 2100.
#
#


from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        data1 = date1.split('-')
        data2 = date2.split('-')
        y1, m1, d1 = data1[0], data1[1], data1[2]
        y2, m2, d2 = data2[0], data2[1], data2[2]
        date_format = "%m/%d/%Y"
        a = datetime.strptime('{}/{}/{}'.format(m1, d1, y1), date_format)
        b = datetime.strptime('{}/{}/{}'.format(m2, d2, y2), date_format)
        delta = abs(b - a)
        return delta.days
        
