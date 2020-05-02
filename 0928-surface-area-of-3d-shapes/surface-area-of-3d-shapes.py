# On a N * N grid, we place some 1 * 1 * 1 cubes.
#
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
#
# Return the total surface area of the resulting shapes.
#
#  
#
#
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: [[2]]
# Output: 10
#
#
#
# Example 2:
#
#
# Input: [[1,2],[3,4]]
# Output: 34
#
#
#
# Example 3:
#
#
# Input: [[1,0],[0,2]]
# Output: 16
#
#
#
# Example 4:
#
#
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
#
#
#
# Example 5:
#
#
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
#
#
#  
#
# Note:
#
#
# 	1 <= N <= 50
# 	0 <= grid[i][j] <= 50
#
#
#
#
#
#
#


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                a = grid[i][j-1] if j>=1 else 0
                b = grid[i-1][j] if i>=1 else 0
                c = grid[i][j+1] if j+1<n else 0
                d = grid[i+1][j] if i+1<m else 0
                if grid[i][j]:
                    for neighbour in [a,b,c,d]:
                        if grid[i][j] > neighbour:
                            res += grid[i][j] - neighbour
                    res += 2 # Top and bottom areas
        return res
