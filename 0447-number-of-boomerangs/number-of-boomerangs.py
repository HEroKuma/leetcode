# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
#
#
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
#
#
#  
#


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p0 in points:
            distmap = collections.defaultdict(int)
            for p1 in points:
                dist = (p0[0]-p1[0]) ** 2 + (p0[1]-p1[1]) ** 2
                distmap[dist] += 1 # Number of points that are dist far away from current point p0
            for p in distmap:
                res += distmap[p] * (distmap[p]-1)
        
        return res
