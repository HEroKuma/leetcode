# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        _list = []
        if root == None:
            return 0
        def trace(root, leaf, p):
            if root.left != None:
                leaf = trace(root.left, leaf, 'l')
            if root.right != None:
                leaf = trace(root.right, leaf, 'r')
            if root.left == None and root.right == None:
                if p == 'l':
                    leaf.append(root.val)
            return leaf
        _list = trace(root, _list, 'r')
        return sum(_list)
