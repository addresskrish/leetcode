class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s=bin(n)[2:]
        if n<0:
            return False
        if s.count('1')==1:
            return True
        return False