# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head # setting up 2 pointers
        prev = None # to help to get to the previous nodes after traversing
        while fast and fast.next: #while both exist
            fast = fast.next.next #shift it to the right twice, this may be Null
            temp = slow.next #stores slows next position
            slow.next = prev #its next position is then set to previous so it reverses
            prev = slow # so we know where the slow is at 
            slow = temp
            # so we traverse across the linked list and as we move across to get half way
            # we also are flipping the order
            # so we will have 2 split linked lists
        
        res = 0
        while slow: #not null, can be prev too
            res = max(res, prev.val + slow.val)
            #prev.val is left linked list and slow.val is the right
            slow = slow.next
            prev = prev.next
        return res


