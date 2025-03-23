# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        preLeftNode, leftNode, rightNode, afterRightNode = None, head, head, None

        while rightNode:
            for i in range(k - 1):
                rightNode = rightNode.next
                if rightNode is None:
                    return head

            if preLeftNode is None:
                head = rightNode

            afterRightNode = rightNode.next
            self.reverseNodes(preLeftNode,  leftNode, afterRightNode, k)

            preLeftNode = leftNode
            leftNode, rightNode = afterRightNode, afterRightNode

        return head

    def reverseNodes(self, preStart, start, afterEnd, k):
        firstNode, secondNode = start, start.next

        for i in range(k - 1):
            thirdNode = secondNode.next

            secondNode.next = firstNode

            firstNode = secondNode
            secondNode = thirdNode

        start.next = afterEnd
        if preStart:
            preStart.next = firstNode