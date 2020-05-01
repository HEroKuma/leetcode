class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        dis = 0
        for i, j in enumerate(points):
            if i != len(points)-1:
                x = points[i]
                y = points[i+1]
                x_d = abs(x[0]-y[0])
                y_d = abs(x[1]-y[1])
                move = min(x_d, y_d)
                dis += move
                if x_d != y_d:
                    dis += abs(x_d - y_d)
        return dis