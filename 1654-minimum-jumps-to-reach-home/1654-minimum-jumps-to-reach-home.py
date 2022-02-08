import time
from collections import defaultdict
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        seen = set([0, False])
            
        def validpos(pos, back):
            return 0 <= pos <= 6000 and (pos, back) not in seen and pos not in forbidden

        def bfs():
            stack = [[0,False,0]]
            count = 1
            while stack:
                for i in range(len(stack)):
                    pos, back, steps = stack.pop(0)
                    if pos == x:
                        return steps
                    if validpos(pos + a, False):
                        stack.append([pos + a, False, steps + 1])
                        seen.add((pos + a, back))
                    if not back and validpos(pos - b, True):
                        stack.append([pos - b, True, steps + 1])
                        seen.add((pos - b, True))
            return -1

        return bfs()