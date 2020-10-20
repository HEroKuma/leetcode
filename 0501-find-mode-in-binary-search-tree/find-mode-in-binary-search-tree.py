# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
#
# 	The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# 	The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# 	Both the left and right subtrees must also be binary search trees.
#
#
#  
#
# For example:
# Given BST [1,null,2,2],
#
#
#    1
#     \
#      2
#     /
#    2
#
#
#  
#
# return [2].
#
# Note: If a tree has more than one mode, you can return them in any order.
#
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        self._count = {}
        
        def dfs(root):
            if root is None:
                return
            if root.val not in self._count:
                self._count[root.val] = 1
            else:
                self._count[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        m = max([i for i in self._count.values()])
        ans = []
        for i, j in self._count.items():
            if j == m:
                ans.append(i)
                
        return ans
