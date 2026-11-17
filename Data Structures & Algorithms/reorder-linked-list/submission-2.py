# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # here slow demarcates the last node of the original
        # list not to be reversed

        prev = None
        curr = slow.next

        i = 0
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        slow.next = None
        # now prev is at the start of the reversed 2nd half
        curr = head

        
        while prev:
            print(f"{prev.val}")
            print(f"{curr.val}")

            prevTemp = prev.next
            currTemp = curr.next

            curr.next = prev
            prev.next = currTemp
            curr = currTemp
            prev = prevTemp
        # while prev:
        #     print(f"{prev.val}")
        #     prev = prev.next
        return


