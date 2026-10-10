# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        def mergeTwoLists(l1, l2):
            if (l1==None):
                return l2
            if (l2==None):
                return l1
            if (l1.val>l2.val):
                temp=l1
                l1=l2
                l2=temp
            res=l1
            while(l1!=None and l2!=None):
                while(l1!=None and l1.val<=l2.val):
                    temp=l1
                    l1=l1.next
                temp.next=l2
                temp2=l1
                l1=l2
                l2=temp2
            return res
        def findmiddle(head1):
            slow=head1
            fast=head1.next
            while(fast!=None and fast.next!=None):
                slow=slow.next
                fast=fast.next.next
            return slow
        
        if head==None or head.next==None:
            return head
        middle=findmiddle(head)
        lefthead=head
        righthead=middle.next
        middle.next=None
        lefthead=self.sortList(lefthead)
        righthead=self.sortList(righthead)
        return mergeTwoLists(lefthead,righthead)