class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        r = j = k = 0; p = -1
        for i, t in enumerate(fruits):
            if t != fruits[j]:
                if t != p: k = j
                p,j = fruits[j],i
            r = max(r, i - k + 1)
        return r