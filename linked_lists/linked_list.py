"""
Project    : interview-sandbox
File       : linked_list.py.py
Created by : louise
On         : 7/15/19
At         : 2:48 PM
"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


def create_linked_list(nums):
    if nums:
        head = Node(data=nums[0])
        l = LinkedList(head=head)
        cur = head
        for n in nums[1:]:
            cur.next = Node(data=n)
            cur = cur.next
    else:
        l = LinkedList()
    return l


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    l = create_linked_list(nums)
    l.print_list()

