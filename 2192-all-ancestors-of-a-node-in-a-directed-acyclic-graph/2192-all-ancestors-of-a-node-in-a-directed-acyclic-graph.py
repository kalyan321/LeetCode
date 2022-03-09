from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, v):
            if node != v:
                self.g[node].append(v)
            self.visited[v] = True
            for nei in self.d[v]:
                if not self.visited[nei]:
                    l = dfs(node, nei)
        self.d = defaultdict(list)
        self.g = defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1] 
            self.d[v].append(u)
        for i in range(n):
            self.visited = [False] * n
            dfs(i, i)
        return [sorted(self.g[i]) for i in range(n)]