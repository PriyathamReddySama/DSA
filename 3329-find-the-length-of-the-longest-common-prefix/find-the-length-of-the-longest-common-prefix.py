class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        # Store all prefixes of arr1 numbers
        prefixes = set()
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10  # Chop off last digit to get next prefix
        
        # Check each prefix of arr2 numbers against the set
        best = 0
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    best = max(best, len(str(num)))
                    break  # Longest prefix for this num already found
                num //= 10
        
        return best