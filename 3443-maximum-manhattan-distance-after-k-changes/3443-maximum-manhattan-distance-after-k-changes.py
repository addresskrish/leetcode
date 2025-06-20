class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def solve(d1, d2, x, s):
            ans = 0
            maxi = 0
            for ch in s:
                if ch == d1 or ch == d2:
                    ans += 1
                else:
                    if x > 0:
                        ans += 1
                        x -= 1
                    else:
                        ans -= 1
                maxi = max(maxi, ans)
            return maxi

        directions = [('N', 'E'), ('N', 'W'), ('S', 'E'), ('S', 'W')]
        ans = 0
        for d1, d2 in directions:
            temp = k
            ans = max(ans, solve(d1, d2, temp, s))
        return ans