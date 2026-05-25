class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        prefix = [0] * (n + 1)
        prefix[1] = 1

        for j in range(1, n):
            if s[j] == '0':
                lo = max(0, j - maxJump)
                hi = j - minJump
                if hi >= 0:
                    reachable[j] = (prefix[hi + 1] - prefix[lo]) > 0
            prefix[j + 1] = prefix[j] + (1 if reachable[j] else 0)

        return reachable[n - 1]