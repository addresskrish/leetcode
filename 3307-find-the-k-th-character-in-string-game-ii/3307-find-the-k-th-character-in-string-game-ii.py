class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1

        num = k
        bt = 0
        while num:
            num //= 2
            bt += 1
        ans = 0
        for i in range(bt) :
            if (k>>i)&1:
                ans += operations[i]
        return chr(ord('a') + (ans % 26))