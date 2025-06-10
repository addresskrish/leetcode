class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

        max_odd = max([value for key, value in freq.items() if value % 2 == 1])
        min_even = min([value for key, value in freq.items() if value % 2 == 0])

        return max_odd - min_even

if __name__ == '__main__':
    s = Solution()
    s.maxDifference("aaaaabbc")