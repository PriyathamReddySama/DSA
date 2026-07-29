class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
        
        n = len(s)
        count = Counter(s)
        
        # Determine half-counts and middle character
        half_count = {}
        middle = ''
        for c, cnt in count.items():
            if cnt % 2 == 1:
                middle = c
            half_count[c] = cnt // 2
        
        half_len = n // 2
        
        # Cap for comparisons - anything >= k is "big enough", avoids overflow
        CAP = k + 1
        
        def capped_mul(a, b):
            if a >= CAP:
                return CAP
            result = a * b
            return result if result < CAP else CAP
        
        def count_permutations(counts, length):
            # multinomial coefficient length! / (c1! c2! ... ck!)
            # computed via sequential binomial coefficients, capped at CAP
            result = 1
            remaining = length
            for c, cnt in counts.items():
                if cnt == 0:
                    continue
                binom = 1
                for i in range(1, cnt + 1):
                    binom = binom * (remaining - cnt + i) // i
                    if binom >= CAP:
                        binom = CAP
                        break
                result = capped_mul(result, binom)
                remaining -= cnt
                if result >= CAP:
                    return CAP
            return result
        
        # Check total distinct permutations of the half multiset
        total = count_permutations(half_count, half_len)
        if total < k:
            return ""
        
        chars_sorted = sorted(half_count.keys())
        half_result = []
        remaining_len = half_len
        
        for pos in range(half_len):
            placed = False
            for c in chars_sorted:
                if half_count[c] == 0:
                    continue
                # tentatively place c
                half_count[c] -= 1
                remaining_len -= 1
                
                cnt = count_permutations(half_count, remaining_len)
                
                if cnt >= k:
                    half_result.append(c)
                    placed = True
                    break
                else:
                    k -= cnt
                    half_count[c] += 1
                    remaining_len += 1
            
            if not placed:
                return ""
        
        half_str = ''.join(half_result)
        return half_str + middle + half_str[::-1]