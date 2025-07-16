class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd, even, odd_even, even_odd = 0, 0, 0, 0
        for num in nums:
            if num % 2:
                odd += 1
                odd_even = even_odd + 1 
            else:
                even += 1
                even_odd = odd_even + 1
        return max(odd, even, odd_even, even_odd)