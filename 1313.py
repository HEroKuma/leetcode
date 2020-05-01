class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(0, len(nums), 2):
            t = [nums[i+1]]*nums[i]
            l+=t
        return l