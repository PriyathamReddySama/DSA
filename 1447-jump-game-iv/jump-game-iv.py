from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        # Group indices by their value
        groups = defaultdict(list)
        for i, val in enumerate(arr):
            groups[val].append(i)
        
        visited = {0}
        queue = deque([(0, 0)])  # (index, steps)
        
        while queue:
            i, steps = queue.popleft()
            
            # Check if we've reached the end
            if i == n - 1:
                return steps
            
            # Neighbor 1: i + 1
            if i + 1 < n and i + 1 not in visited:
                visited.add(i + 1)
                queue.append((i + 1, steps + 1))
            
            # Neighbor 2: i - 1
            if i - 1 >= 0 and i - 1 not in visited:
                visited.add(i - 1)
                queue.append((i - 1, steps + 1))
            
            # Neighbor 3: same-value indices
            for j in groups[arr[i]]:
                if j not in visited:
                    visited.add(j)
                    queue.append((j, steps + 1))
            
            # Critical optimization: clear the group after processing
            groups[arr[i]].clear()
        
        return -1  # unreachable given problem constraints