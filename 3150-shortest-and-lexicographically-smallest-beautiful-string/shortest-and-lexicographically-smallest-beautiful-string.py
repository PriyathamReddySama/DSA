class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        # Find the positions of all 1s
        ones = []

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        # If there are not enough 1s
        if len(ones) < k:
            return ""

        # Store the best substring
        best = ""

        # Take k 1s at a time
        for i in range(len(ones) - k + 1):

            # Start = first 1
            start = ones[i]

            # End = kth 1
            end = ones[i + k - 1]

            # Get the substring
            candidate = s[start:end + 1]

            # Choose the best candidate
            if best == "":
                best = candidate

            elif len(candidate) < len(best):
                best = candidate

            elif len(candidate) == len(best) and candidate < best:
                best = candidate

        return best