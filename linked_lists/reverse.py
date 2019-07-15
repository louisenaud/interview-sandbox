"""
Project    : interview-sandbox
File       : reverse.py.py
Created by : louise
On         : 7/15/19
At         : 2:47 PM
"""
from linked_lists.linked_list import Node, LinkedList, create_linked_list


def reverse(llist):
    cur = llist.head
    rev = None
    while cur:
        n = cur.next
        cur.next = rev
        rev = cur
        cur = n

    return LinkedList(head=rev)


def reverse_rec(cur):
    if not cur or not cur.next:
        return cur

    n_head = reverse_rec(cur.next)
    return


if __name__ == "__main__":
    llist = create_linked_list([1, 2, 3, 4, 5])

    rev = reverse(llist=llist)
    rev.print_list()
