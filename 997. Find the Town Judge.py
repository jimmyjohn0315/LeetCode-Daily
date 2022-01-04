class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = Counter(y for _, y in trust)
        outDegree = Counter(x for x, _ in trust)
        
        for i in range(1, n + 1):
            if inDegree[i] - outDegree[i] == n - 1:
                return i
        return -1
