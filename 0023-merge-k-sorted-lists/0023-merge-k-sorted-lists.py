# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists)==0:
            return 

        import heapq
        min_heap = []
        for i , node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i , node))

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            node_val, index,smallest_node = heapq.heappop(min_heap)
            curr.next = smallest_node
            curr = curr.next

            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, index , smallest_node.next))

        return dummy.next