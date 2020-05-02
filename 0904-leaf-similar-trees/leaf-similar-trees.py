# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#  
# Constraints:
#
#
# 	Both of the given trees will have between 1 and 200 nodes.
# 	Both of the given trees will have values between 0 and 200
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf_1 = []
        leaf_2 = []
        def leaforder(root, l):
            if root is None:
                return l
            if root.left is None and root.right is None:
                l.append(root.val)
            l = leaforder(root.left, l)
            l = leaforder(root.right, l)
            return l
        leaf_1 = leaforder(root1, leaf_1)
        leaf_2 = leaforder(root2, leaf_2)
        # print(leaf_1)
        # print(leaf_2)
        return True if leaf_1 == leaf_2 else False
