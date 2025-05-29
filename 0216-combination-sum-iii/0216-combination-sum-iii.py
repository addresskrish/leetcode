class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def findComb(i, k, n, curr, ans, visit):
            if sum(curr) == n and len(curr) == k:
                ans.append(curr.copy())
                return

            if len(curr) > k or i > 9 or sum(curr) > n:
                return

            if(len(curr) <= k):
                for i in range(i, 10):
                    findComb(i + 1, k, n, curr + [i], ans, visit)

        ans = []
        curr = []
        visit = set()
        findComb(1, k, n, curr, ans, visit)
        return ans