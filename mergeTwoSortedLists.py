import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        nnode = ListNode()
        output = nnode
        while list1 and list2:
            if list2.val < list1.val:
                output.next = list2
                list2 = list2.next
            else:
                output.next = list1
                list1 = list1.next
            output = output.next
        if list1:
            output.next = list1
        elif list2:
            output.next = list2
        return nnode.next

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        