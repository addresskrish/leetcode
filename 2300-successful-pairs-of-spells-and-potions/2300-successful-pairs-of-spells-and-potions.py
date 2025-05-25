class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        for i in range(len(potions)):
            quo = success // potions[i]
            rem = success % potions[i]
            potions[i] = quo
            if rem:
                potions[i] += 1

        potions.sort()
        res = []
        for i in spells:
            idx = bisect_right(potions, i)
            res.append(idx)

        return res 