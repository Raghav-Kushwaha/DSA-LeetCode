# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def findKthNode(temp,k):
            k-=1
            while (temp!=None and k>0):
                k-=1
                temp=temp.next
            return temp

        def reverse(head):
            prev = None
            curr = head
    
            while curr:
                next_node = curr.next  
                curr.next = prev       
                prev = curr            
                curr = next_node
            return prev    

        prevnode=None
        temp=head

        while(temp!=None):
            kthNode=findKthNode(temp,k)
            if (kthNode==None):
                prevnode.next=temp
                break
            nextnode=kthNode.next
            kthNode.next=None
            reverse(temp)
            if (temp==head):
                head=kthNode
            else:
                prevnode.next=kthNode
            prevnode=temp
            temp=nextnode
        return head