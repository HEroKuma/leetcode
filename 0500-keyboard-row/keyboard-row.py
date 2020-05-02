# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
#  
#
#
#  
#
# Example:
#
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
#  
#
# Note:
#
#
# 	You may use one character in the keyboard more than once.
# 	You may assume the input string will only contain letters of alphabet.
#
#


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = set('qwertyuiop')
        home = set('asdfghjlkl')
        bot = set('zxcvbnm')
        ans = []
        for w in words:
            word = set(w.lower())
            # print(word)
            for j in (top, home, bot):
                if word <= j:
                    ans.append(w)
        
        return ans
