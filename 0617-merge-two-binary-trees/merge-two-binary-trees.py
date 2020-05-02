# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
#
#
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
#
#
#  
#
# Note: The merging process must start from the root nodes of both trees.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if (t1 == t2 == None):
            return None
        t3 = TreeNode(None)
        self.merge(t1, t2, t3)
        self.removeNone(t3)           
        return t3

    def merge(self, t1, t2, t3):
        if t1 is not None and t2 is not None:
            t3.val = t1.val + t2.val
            t3.left = TreeNode(None)
            t3.right = TreeNode(None)
            self.merge(t1.left, t2.left, t3.left)
            self.merge(t1.right, t2.right, t3.right)
            
        elif t1 is not None:
            t3.val = t1.val
            t3.left = TreeNode(None)
            t3.right = TreeNode(None)
            self.merge(t1.left, t2, t3.left)
            self.merge(t1.right, t2, t3.right)
            
        elif t2 is not None:
            t3.val = t2.val
            t3.left = TreeNode(None)
            t3.right = TreeNode(None)
            self.merge(t1, t2.left, t3.left)
            self.merge(t1, t2.right, t3.right)
    
    def removeNone(self, t3: TreeNode):
        if (t3 == None):
            return
        if (t3.left != None and t3.left.val == None):
            t3.left = None    
        if (t3.right != None and t3.right.val == None):
            t3.right = None 
        self.removeNone(t3.left)
        self.removeNone(t3.right)
