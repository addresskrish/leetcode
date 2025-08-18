from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = nums[i], nums[j]
                    next_nums = [nums[k] for k in range(n) if k != i and k != j]

                    results = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS: results.append(a / b)
                    if abs(a) > EPS: results.append(b / a)

                    for res in results:
                        if solve(next_nums + [res]):
                            return True
            return False

        return solve([float(c) for c in cards])