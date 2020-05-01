class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = 0
        for j in J:
            for s in S:
                if j == s:
                    c+=1
        return c