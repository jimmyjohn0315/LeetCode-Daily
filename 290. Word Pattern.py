class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        if len(pattern) != len(arr):
            return False
        dic1 = {}
        for i in range(len(pattern)):
            if pattern[i] not in dic1:
                dic1[pattern[i]] = arr[i]
            elif dic1[pattern[i]] != arr[i]:
                return False
        dic2 = {}
        for i in range(len(arr)):
            if arr[i] not in dic2:
                dic2[arr[i]] = pattern[i]
            elif dic2[arr[i]] != pattern[i]:
                return False
        return True
