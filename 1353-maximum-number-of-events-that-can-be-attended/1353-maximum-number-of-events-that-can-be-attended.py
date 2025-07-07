class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()         
        heap = []              
        day = res = i = 0
        n = len(events)

        while i < n or heap:
            if not heap:                
                day = events[i][0]

            while i < n and events[i][0] <= day:
                heappush(heap, events[i][1])
                i += 1

            heappop(heap)                  
            res += 1
            day += 1                       

            while heap and heap[0] < day:
                heappop(heap)
        
        return res