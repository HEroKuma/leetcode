# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#
# Given tree t:
#
#
#    4 
#   / \
#  1   2
#
# Return true, because t has the same structure and node values with a subtree of s.
#
#  
#
# Example 2:
# Given tree s:
#
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#
# Given tree t:
#
#
#    4
#   / \
#  1   2
#
# Return false.
#
#  
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        
        def checkTree(r1, r2):
            if not r1 and not r2:
                return True
            elif r1 and not r2 or r2 and not r1:
                return False
            
            if r1.val != r2.val:
                return False
            
            return checkTree(r1.left, r2.left) and checkTree(r1.right, r2.right)
        
        def dfs(s, t):
            if not s:
                return False
            
            if s.val == t.val and checkTree(s, t):
                return True
            
            return dfs(s.left, t) or dfs(s.right, t)
            
        return dfs(s, t)
