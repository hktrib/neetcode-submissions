# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        else:

            # find length of list

            i = 0
            curr = head
            while curr:
                curr = curr.next
                i += 1
            
            k = i - n
            prev = None
            curr = head
            if k == 0:
                return curr.next
            else:

                i = 0
                while i != k:
                    prev = curr
                    curr = curr.next
                    i += 1

                prev.next = curr.next
                return head

