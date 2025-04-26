class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = 0
        m = 0
        for change in gain:
            a += change
            m = max(m, a)
        return m