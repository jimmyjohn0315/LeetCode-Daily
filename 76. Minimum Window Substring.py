class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        ft = Counter(t)
        fs = {}
        i, j = 0, 0
        start, end = -n - 1, -1
        while j < n:
            if s[j] in fs:
                fs[s[j]] += 1
            else:
                fs[s[j]] = 1
            while self.check(fs, ft):
                if j - i < end - start:
                    start, end = i, j
                fs[s[i]] -= 1
                i += 1
            j += 1
              
        return s[start:end + 1]
    
    def check(self, fs, ft):
        for k in ft.keys():
            if k not in fs or fs[k] < ft[k]:
                return False
        return True
