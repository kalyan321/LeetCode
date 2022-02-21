# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.summ = 0
        def rootToLeaf(root, sub):
            if root is None:
                return
            if not root.left and not root.right:
                self.summ += int(sub + str(root.val))
            rootToLeaf(root.left, sub + str(root.val))
            rootToLeaf(root.right, sub + str(root.val))
        rootToLeaf(root, '')
        return self.summ