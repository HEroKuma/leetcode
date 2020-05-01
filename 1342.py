class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.cacu(num, 0)

    def cacu(self, num, step):
        if num is 0:
            return step
        if num % 2 is 0:
            # print(num)
            return self.cacu(num // 2, step + 1)
        if num % 2 is 1:
            # print(num)
            return self.cacu(num - 1, step + 1)