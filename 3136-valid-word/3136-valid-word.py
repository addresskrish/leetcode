class Solution:
    def isValid(self, word: str) -> bool:
        return (
            len(word) >= 3 and 
            word.isalnum() and 
            any(c in 'aeiouAEIOU' for c in word) and 
            any(c.isalpha() and c.lower() not in 'aeiou' for c in word)
        )