# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        l = []
        def smallestLeaf(root, sub):
            if root:
                if not root.left and not root.right:
                    l.append(chr(root.val + 97) + sub)
                smallestLeaf(root.left, chr(root.val + 97) + sub)
                smallestLeaf(root.right, chr(root.val + 97) + sub)
        smallestLeaf(root, '')
        return min(l)