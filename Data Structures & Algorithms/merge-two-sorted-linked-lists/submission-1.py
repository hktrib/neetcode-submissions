# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            # set node from old node to the new min(list1, list2)
            # and iterate to next to grab next min value
            node = node.next
        

        # deal with remainder of either list1 or list2

        # this sets the next of the node to 
        # list1 or list2 depending on which one of them is
        # not None. Only can be so based on the previous loop condition
        # of while list1 and list2
        node.next = list1 or list2

        return dummy.next