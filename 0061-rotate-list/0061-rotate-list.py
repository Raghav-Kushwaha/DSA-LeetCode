# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or head.next==None:
            return head 
        temp=head
        n=1
        while(temp.next!=None):
            temp=temp.next
            n+=1
        temp.next=head
        k=k%n
        m=(n-k)
        for i in range(m):
            temp=temp.next
        new_head=temp.next
        temp.next=None
        return new_head
