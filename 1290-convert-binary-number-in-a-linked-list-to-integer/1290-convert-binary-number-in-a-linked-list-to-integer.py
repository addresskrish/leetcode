# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        n=0
        while head!=None:
            n=(n*10)+head.val
            head=head.next
        r=0
        c=0
        while n!=0:
            r+=(n%10)*(2**c)
            c+=1
            n//=10
        return r