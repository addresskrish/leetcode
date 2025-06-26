class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        val = 0
        res = 0
        bit_position = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                res += 1
            else:
                if (val + (1 << bit_position)) <= k:
                    val += (1 << bit_position)
                    res += 1
            bit_position += 1

        return res