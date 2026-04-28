# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        node = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Approach Merge 2 Lists: Time O(n * k) Mem O(1)
        # if not len(lists):
        #     return None

        # for i in range(1, len(lists)):
        #     lists[i] = self.mergeTwoLists(lists[i - 1], lists[i])
        
        # return lists[-1]

        # Approach Merge 2 Lists V2: Time O(nlogk) Mem(O1)
        if not len(lists):
            return None
        
        # Until lists has only one. That is the sorted list
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]