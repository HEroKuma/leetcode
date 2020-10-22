# A boomerang is a set of 3 points that are all distinct and not in a straight line.
#
# Given a list of three points in the plane, return whether these points are a boomerang.
#
#  
#
# Example 1:
#
#
# Input: [[1,1],[2,3],[3,2]]
# Output: true
#
#
#
# Example 2:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: false
#
#
#  
#
# Note:
#
#
# 	points.length == 3
# 	points[i].length == 2
# 	0 <= points[i][j] <= 100
#
#
#
#  
#


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        
        return (x0-x1)*(y0-y2) != (x0-x2)*(y0-y1)
