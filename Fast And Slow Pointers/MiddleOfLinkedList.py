'''
Middle of Linked List, LC #876
https://leetcode.com/problems/middle-of-the-linked-list/
'''

import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach 1: Two Passes
def middleNode_2pass(head: ListNode) -> ListNode:
    length = 0
    ptr = head
    while ptr:
        length += 1
        ptr = ptr.next

    ptr = head
    for i in range(math.ceil(length / 2)):
        ptr = ptr.next

    return ptr

# Approach 2: Fast & Slow Pointers
def middleNode_ptrs(head: ListNode) -> ListNode:
    sp = head  # slow pointer
    fp = head  # fast pointer
    while fp:
        if fp.next:
            sp = sp.next
            fp = fp.next.next
        else:
            break

    return sp