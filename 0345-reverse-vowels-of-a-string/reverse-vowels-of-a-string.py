# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
#
# Input: "hello"
# Output: "holle"
#
#
#
# Example 2:
#
#
# Input: "leetcode"
# Output: "leotcede"
#
#
# Note:
# The vowels does not include the letter "y".
#
#  
#


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i' ,'o','u', 'A', 'E', 'I' , 'O', 'U']
        s = list(s)
        vpos=[]
        vword=[]
        for index, char in enumerate(s):
            if char in vowel:
                vpos.append(index)
                vword.append(char)

        for i in vpos:
            s[i]=vword.pop()

        return "".join(s)
