'''
Leetcode #234: Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time, O(n) space
def isPalindrome_list(self, head: ListNode) -> bool:
    vals = []
    ptr = head
    while ptr:
        vals.append(ptr.val)
        ptr = ptr.next
    return vals == vals[::-1]


# O(n) time, O(1) space, but slower than creating array
# find midpoint, then reverse the 2nd half of the linkedlist and compare
def isPalindrome_constantspace(head: ListNode) -> bool:
    # O(1) approach: find midpoint, reverse 2nd half of LL
    sp = fp = head
    while fp and fp.next:
        sp = sp.next
        fp = fp.next.next
    # sp now points to midpoint
    # then reverse 2nd half of LL
    node = sp
    prev = None
    while node:
        nn = node.next  # store next node
        node.next = prev  # point current node to prev
        prev = node
        node = nn

    # mid now points head of rev LL
    ptr1 = head
    ptr2 = prev
    while (ptr1 and ptr2):
        if ptr1.val == ptr2.val:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        else:
            return False
    return True


def printLL(head):
    print('linkedlist:')
    ptr = head
    while ptr:
        print(ptr.val, end=' ')
        ptr = ptr.next
    print()
