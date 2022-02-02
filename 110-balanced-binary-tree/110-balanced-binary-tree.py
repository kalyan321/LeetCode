# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isbalanced(root):
            if root is None:
                return 0
            l = isbalanced(root.left)
            r = isbalanced(root.right)
            if abs(l - r) > 1 or l == -1 or r == -1:
                return -1
            return max(l, r) + 1
        return False if isbalanced(root) == -1 else True