# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
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