class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap = []
        right_heap = []
        left_ptr = 0
        right_ptr = len(costs) - 1
        total_cost = 0
        for _ in range(k):
            while len(left_heap) < candidates and left_ptr <= right_ptr:
                heapq.heappush(left_heap, costs[left_ptr])
                left_ptr += 1
            
            while len(right_heap) < candidates and left_ptr <= right_ptr:
                heapq.heappush(right_heap, costs[right_ptr])
                right_ptr -= 1
            
            left_min = left_heap[0] if left_heap else float('inf')
            right_min = right_heap[0] if right_heap else float('inf')

            if left_min <= right_min:
                total_cost += heapq.heappop(left_heap)
            else:
                total_cost += heapq.heappop(right_heap)
            
        return total_cost