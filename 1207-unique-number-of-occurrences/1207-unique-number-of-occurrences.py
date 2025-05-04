class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uni_dict = {}

        for i in arr:
            if i in uni_dict:
                uni_dict[i] += 1
            else:
                uni_dict[i] = 1

        vals = uni_dict.values()
        return len(vals) == len(set(vals))