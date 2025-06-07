class Solution:
    def numTilings(self, n: int) -> int:
        prev, t, b = 0, 0, 0
        curr = 1
        for i in range(1, n + 1):
            tmp = curr
            prev_t = t
            curr += prev + t + b
            t = prev + b
            b = prev + prev_t
            prev = tmp

        return curr % ((10 ** 9) + 7)