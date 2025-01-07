class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        
        res = 0
        xc = x
        while x > 0 :
            res = (res * 10) + (x % 10)
            x //= 10
        
        return res == xc