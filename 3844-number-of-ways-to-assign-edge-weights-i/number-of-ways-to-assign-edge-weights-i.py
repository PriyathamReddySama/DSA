from collections import deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        if n == 1:
            return 0

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS from root to find max depth
        max_depth = 0
        visited = [False] * (n + 1)
        queue = deque([(1, 0)])  # (node, depth)
        visited[1] = True

        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    queue.append((nei, depth + 1))

        # 2^(max_depth - 1) mod MOD
        return pow(2, max_depth - 1, MOD)