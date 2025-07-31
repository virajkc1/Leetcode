# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head #then we return the None or just the head
        odd = head
        even = even_head = head.next # so its at the next head
        while even and even.next: #while this is true do pointer switching
            odd.next = even.next #odds next node will be 2 jumps and thats one jump for even
            odd = odd.next # so now odd moves 2 positions 
            even.next = odd.next # then jumps 2 for odd
            even = even.next # so now we moved the even next 
        odd.next = even_head #links the 2 separate lists 
        return head

