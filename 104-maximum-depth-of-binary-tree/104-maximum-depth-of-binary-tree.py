# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(root):
            if(root is None):return 0
            l=depth(root.left)
            r=depth(root.right)
            if(l>r):
                return l+1
            else:
                return r+1
        return depth(root)