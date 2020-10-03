# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
#  
# Example 1:
#
#
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#
#
# Example 2:
#
#
# Input: grid = [[1]]
# Output: 4
#
#
# Example 3:
#
#
# Input: grid = [[1,0]]
# Output: 4
#
#
#  
# Constraints:
#
#
# 	row == grid.length
# 	col == grid[i].length
# 	1 <= row, col <= 100
# 	grid[i][j] is 0 or 1.
#
#


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        table = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans+=4
                    for k in table:
                        if 0 <= i+k[0] < len(grid) and 0 <= j+k[1] < len(grid[0]):
                            if grid[i+k[0]][j+k[1]] == 1:
                                # print(i+k[0], j+k[1])
                                ans-=1
        return ans
