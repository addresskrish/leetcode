class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        x=1
        while x<=n:
            if x==n:
                return True
            x*=4
        return False