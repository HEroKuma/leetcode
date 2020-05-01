class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = 1
        p = 0
        for i in str(n):
            m *= int(i)
            p += int(i)

        return m - p