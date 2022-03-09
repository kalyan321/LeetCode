from collections import defaultdict
class Solution(object):
    def eventualSafeNodes(self, graph):
        d = defaultdict(int)
        
        def dfs(v):
            if d[v] == 1:
                return False
            if d[v] == 2:
                return True
            d[v] = 1
            for nei in graph[v]:
                if d[nei] == 2:
                    continue
                elif d[nei] == 1 or not dfs(nei):
                    return False
            d[v] = 2
            return True
        return filter(dfs, range(len(graph)))