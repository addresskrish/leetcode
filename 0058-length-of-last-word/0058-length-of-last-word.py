class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.strip().split(' ')
        if (len(a) > 0):
            return len(a[len(a) - 1])
        else:
            return -1