# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def findLen(head) -> int:
            length = 0
            while head:
                length+=1
                head = head.next

            return length
        
        length = findLen(head);

        n = length - n

        if n == 0:
            return head.next

        cur = head
        while n-1 > 0:
            cur = cur.next
            n-=1

        cur.next = cur.next.next

        return head

        