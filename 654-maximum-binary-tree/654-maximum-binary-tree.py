# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def getMaxPos(start, end):
            maxi = float('-inf')
            pos = -1
            for i in range(start, end + 1):
                if maxi < nums[i]:
                    maxi = nums[i]
                    pos = i
            return pos
        def constructTree(l,r,root):
            # if l > r:
            #     return root
            pos = getMaxPos(l, r)
            root = TreeNode(nums[pos])
            if l != pos:
                root.left = constructTree(l, pos-1, root)
            if r != pos:
                root.right = constructTree(pos+1, r, root)
            return root
        return constructTree(0, len(nums) - 1, None)