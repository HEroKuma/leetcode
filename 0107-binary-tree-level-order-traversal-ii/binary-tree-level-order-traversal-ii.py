# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return None
        _dict = []
        ans = []
        def trace(root, depth, _dict):
            if root.left != None:
                _dict =  trace(root.left, depth+1, _dict)
            if root.right != None:
                _dict =  trace(root.right, depth+1, _dict)
            _dict.append((depth, root.val))
            return _dict
        _dict = trace(root, 0, _dict)
        level = max(_dict)[0]
        for i in range(level+1):
            ans.append([])
        for i in _dict:
            ans[level-i[0]].append(i[1])
            
        return ans
