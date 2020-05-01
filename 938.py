# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        sum = self.pre(root, sum, L, R)
        return sum
    def pre(self, root, sum, L, R):
        if root.left is not None:
            sum = self.pre(root.left, sum, L, R)
        # print(root.val, L, R)
        # if L <= root.val <= R:
        #     return sum+=root.val
        # print(root.val)
        if root.right is not None:
            sum = self.pre(root.right, sum, L, R)
        if L <= root.val <= R:
            sum += root.val
        return sum