class Solution:
    def minimumDistance(self, nums):
        pos = defaultdict(list)

        for i, v in enumerate(nums):
            pos[v].append(i)
        ans = float('inf')

        for v, arr in pos.items():
            if len(arr) < 3:
                continue
            
            for i in range(len(arr) - 2):
                dist = 2 * (arr[i+2] - arr[i])
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1
        