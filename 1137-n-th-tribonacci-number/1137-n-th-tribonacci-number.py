class Solution:
    def tribonacci(self, n: int) -> int:
        def memo(n: int, memory = {}) -> int:
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in memory:
                return memory[n]
            memory[n] = memo(n - 1) + memo(n - 2) + memo(n - 3)
            return memory[n]
        return memo(n)