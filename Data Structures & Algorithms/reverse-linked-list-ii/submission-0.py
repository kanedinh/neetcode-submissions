# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Phase 1: Traverse to Left Node
        dummy = ListNode(0, head)
        leftPrev = dummy
        curr = head

        for _ in range(left - 1):
            leftPrev, curr = leftPrev.next, curr.next
        # leftPrev: left of the Left Node
        # curr: Left Node

        # Phase 2: Reverse The Sub-Linked List
        prev = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Phase 3: leftPrev point to Right Node, Left Node point to curr
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next