class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        cnt = 1
        
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                cnt += 1
            else:
                cnt = 2

            if cnt <= 2:
                res.append(s[i])

        return ''.join(res)