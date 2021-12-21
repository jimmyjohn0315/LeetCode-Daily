class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        look = {}
        start, end = 0, 0
        res = 0
        for end in range(n):
            c = s[end]
            if c in look:
                start = max(start, look[c] + 1)
            look[c] = end
            res = max(res, end - start + 1)
        return res
