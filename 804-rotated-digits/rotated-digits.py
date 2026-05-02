from functools import lru_cache

class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {0, 1, 2, 5, 6, 8, 9}
        changes = {2, 5, 6, 9}
        digits = [int(d) for d in str(n)]

        @lru_cache(maxsize=None)
        def dp(pos, tight, changed):
            if pos == len(digits):
                return 1 if changed else 0
            
            limit = digits[pos] if tight else 9
            result = 0
            
            for d in range(0, limit + 1):
                if d not in valid:
                    continue
                result += dp(
                    pos + 1,
                    tight and (d == limit),
                    changed or (d in changes)
                )
            
            return result

        return dp(0, True, False)