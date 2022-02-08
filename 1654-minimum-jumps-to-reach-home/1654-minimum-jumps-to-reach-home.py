import time
from collections import defaultdict
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        seen = set([0, False])
            
        def validpos(pos, back):
            return 0 <= pos <= 6000 and (pos, back) not in seen and pos not in forbidden

        def bfs():
            stack = [[0,False]]
            steps = 0
            while stack:
                for i in range(len(stack)):
                    pos, back = stack.pop(0)
                    if pos == x:
                        return steps
                    if validpos(pos + a, False):
                        stack.append([pos + a, False])
                        seen.add((pos + a, back))
                    if not back and validpos(pos - b, True):
                        stack.append([pos - b, True])
                        seen.add((pos - b, True))
                steps += 1
            return -1

        return bfs()