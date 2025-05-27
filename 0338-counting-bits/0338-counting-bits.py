class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [i.bit_count() for i in range(n + 1)]
        return res