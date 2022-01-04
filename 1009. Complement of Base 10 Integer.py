class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        m = n
        d = 0
        while m != 0:
            m //= 2
            d += 1
        mask = (1 << d) - 1
        return n ^ mask
