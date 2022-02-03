class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        res = []
        if m < n:
            return res
        sCount = [0] * 26
        pCount = [0] * 26
        for i in range(n):
            pCount[ord(p[i]) - ord('a')] += 1
            sCount[ord(s[i]) - ord('a')] += 1
        
        if sCount == pCount:
            res.append(0)
            
        for i in range(1, m - n + 1):
            sCount[ord(s[i-1]) - ord('a')] -= 1
            sCount[ord(s[i+n-1]) - ord('a')] += 1
            if sCount == pCount:
                res.append(i)
                
        return res
