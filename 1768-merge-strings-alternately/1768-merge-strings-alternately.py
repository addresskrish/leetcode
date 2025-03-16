class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        result = ''
        len1 = len(word1)
        len2 = len(word2)

        max_len = max(len1, len2)

        while i < max_len:
            if i < len1:
                result += word1[i]

            if i < len2:
                result += word2[i]
            
            i += 1
        return result