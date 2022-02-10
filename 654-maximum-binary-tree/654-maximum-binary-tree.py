# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def getMaxValPos(start, end):
            maxi = float('-inf')
            pos = -1
            for i in range(start, end + 1):
                if maxi < nums[i]:
                    maxi = nums[i]
                    pos = i
            return pos
        
        def constructTree(start, end):
            pos = getMaxValPos(start, end)
            root = TreeNode(nums[pos])
            if start != pos:
                root.left = constructTree(start, pos-1)
            if end != pos:
                root.right = constructTree(pos+1, end)
            return root


        return constructTree(0, len(nums) - 1)