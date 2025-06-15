class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        max_s = list(s)
        min_s = list(s)
        n = len(s)

        #Max num
        for i in range(n):
            if max_s[i] != "9":
                target = max_s[i]
                for j in range(n):
                    if max_s[j] == target:
                        max_s[j] = "9"
                
                break
        
        #Min num
        if min_s[0] > "1":
            target = min_s[0]
            for i in range(n):
                if min_s[i] == target:
                    min_s[i] = "1"
        
        else:
            for i in range(1, n):
                if min_s[i]>"1":
                    target = min_s[i]
                    for j in range(i,n):
                        if min_s[j]== target:
                            min_s[j]="0"
                    
                    break

        
        max_num = int(''.join(max_s))
        min_num = int(''.join(min_s))

        return max_num - min_num