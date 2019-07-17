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
    # if current node is None -> return None; if cur.next is None: tail node -> set as new head
    if not cur or not cur.next:
        return cur
    # recursive call to next node (exists thanks to last if statement)
    n_head = reverse_rec(cur.next)
    # if node returned here, it means we got the tail of the list, so it is the new head

    # Make current node's next node point to current node to reverse list
    cur.next.next = cur
    # make current node point to None
    cur.next = None
    return n_head


if __name__ == "__main__":
    llist = create_linked_list([1, 2, 3, 4, 5])

    rev = reverse(llist=llist)
    rev.print_list()
