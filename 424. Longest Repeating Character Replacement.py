class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 26
        maxl = 0
        i, j = 0, 0
        while j < n:
            freq[ord(s[j]) - ord('A')] += 1
            maxl = max(maxl, freq[ord(s[j]) - ord('A')])
            if j - i + 1 > maxl + k:
                freq[ord(s[i]) - ord('A')] -= 1
                i += 1
            j += 1
        return j - i
