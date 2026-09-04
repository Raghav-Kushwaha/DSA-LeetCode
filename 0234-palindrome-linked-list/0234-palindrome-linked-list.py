# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def Reverse(head):
            prev=None
            current = head
            while current :
                nextnode=current.next
                current.next=prev
                prev=current
                current=nextnode
            return prev

        slow=head
        fast=head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        
        first=head
        second=Reverse(slow.next)
        while(second!=None):
            if first.val != second.val:
                return False
            first=first.next
            second=second.next
        return True