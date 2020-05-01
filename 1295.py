class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            if len(str(i)) % 2 is 0:
                c += 1

        return c