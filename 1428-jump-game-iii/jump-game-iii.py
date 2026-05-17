from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        queue = deque([start])

        while queue:
            i = queue.popleft()

            # Found a zero
            if arr[i] == 0:
                return True

            # Skip already visited indices
            if i in visited:
                continue
            visited.add(i)

            # Jump right
            if i + arr[i] < n:
                queue.append(i + arr[i])

            # Jump left
            if i - arr[i] >= 0:
                queue.append(i - arr[i])

        return False