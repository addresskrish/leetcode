class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = 0

        pre = [endTime[0] - startTime[0]]
        for i in range(1 ,n):
            pre.append(pre[-1] + endTime[i] - startTime[i])
        
        for i in range(k - 1 , n):
            left = endTime[i -k] if i - k >= 0 else 0
            right = startTime[i + 1] if i + 1 < n else eventTime
            total_duration = pre[i] - (pre[i - k] if i - k >= 0 else 0)
            res = max(res , right - left - total_duration)

        return res