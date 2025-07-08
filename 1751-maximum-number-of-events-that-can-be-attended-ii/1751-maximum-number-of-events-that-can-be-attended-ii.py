class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [event[0] for event in events]
        @lru_cache(None)
        def dfs(i,k_left):
            if i == n or k_left == 0:
                return 0
            res = dfs(i+1,k_left)
            next_index = bisect.bisect_left(starts,events[i][1] + 1)
            res = max(res,dfs(next_index,k_left - 1) + events[i][2])
            return res
        return dfs(0,k)