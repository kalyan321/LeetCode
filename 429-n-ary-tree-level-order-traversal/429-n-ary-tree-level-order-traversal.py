"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        ans = []
        queue = [root]
        while queue:
            l = []
            for i in range(len(queue)):
                ele = queue.pop(0)
                for child in ele.children:
                    queue.append(child)
                l.append(ele.val)
            ans.append(l)
        return ans