# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        def merge2lists(list1 , list2):
            dummy=ListNode(-1)
            res=dummy
            while(list1!=None and list2!=None):
                if list1.val<list2.val:
                    res.next=list1
                    list1=list1.next
                else:
                    res.next=list2
                    list2=list2.next
                res=res.next
            res.next=list1 if list1 else list2
            return dummy.next
        def merge(i):
            if i == len(lists):
                return None
            if i==len(lists)-1:
                return lists[i]
            mergedlist=merge(i+1)
            return merge2lists(lists[i],mergedlist)
        return merge(0)
