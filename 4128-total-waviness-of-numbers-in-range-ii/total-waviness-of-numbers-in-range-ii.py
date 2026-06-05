class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        from functools import lru_cache

        def solve(n):
            s = str(n)
            L = len(s)

            @lru_cache(None)
            def dp(pos, prev2, prev1, started, tight):
                if pos == L:
                    return (1, 0) if started else (0, 0)

                limit = int(s[pos]) if tight else 9
                total_count = 0
                total_waviness = 0

                for d in range(0, limit + 1):
                    n_started = started or d != 0
                    n_tight = tight and (d == limit)

                    if not n_started:
                        cnt, wav = dp(pos + 1, -1, -1, 0, n_tight)
                    else:
                        if prev1 == -1:
                            cnt, wav = dp(pos + 1, -1, d, 1, n_tight)
                        elif prev2 == -1:
                            cnt, wav = dp(pos + 1, prev1, d, 1, n_tight)
                        else:
                            add = 0
                            if prev2 < prev1 > d:
                                add = 1
                            elif prev2 > prev1 < d:
                                add = 1

                            cnt, wav = dp(pos + 1, prev1, d, 1, n_tight)
                            wav += add * cnt

                    total_count += cnt
                    total_waviness += wav

                return total_count, total_waviness

            return dp(0, -1, -1, 0, 1)[1]

        return solve(num2) - solve(num1 - 1)
