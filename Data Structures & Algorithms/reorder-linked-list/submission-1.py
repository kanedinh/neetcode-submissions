# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Brute Force
        # if not head:
        #     return

        # nodes = []
        # node = head
        # while node:
        #     nodes.append(node)
        #     node = node.next
        
        # i = 0
        # j = len(nodes) - 1
        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i += 1
        #     if i >= j:
        #         break
        #     nodes[j].next = nodes[i]
        #     j -= 1
        # nodes[i].next = None

        # Slow & Fast
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        prev = slow.next = None

        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec =  tmp
        
        l, r = head, prev

        while r:
            tmp1, tmp2 = l.next, r.next
            l.next = r
            r.next = tmp1
            l, r = tmp1, tmp2
        
        