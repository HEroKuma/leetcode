class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        p = 0
        for i in s:
            if i is 'L':
                c+=1
            if i is 'R':
                c-=1
            if c is 0:
                p+=1
        return p