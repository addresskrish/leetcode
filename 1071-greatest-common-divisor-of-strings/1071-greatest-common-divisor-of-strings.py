class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        cur = ''
        av = []
        for i in range(len(str1)):
            if (i+1)*str1.count(str1[:i+1])==len(str1):
                cur = str1[:i+1]
                av.append(cur)
        ab = []
        for i in range(len(str2)):
            if (i+1)*str2.count(str2[:i+1])==len(str2):
                cur = str2[:i+1]
                ab.append(cur)
        
        ans = ''
        max_len = 0
        for i in range(len(av)):
            for j in range(len(ab)):
                if av[i] == ab[j]:
                    m = len(av[i])
                    if m > max_len:
                        max_len = m
                        ans = av[i]
        return ans