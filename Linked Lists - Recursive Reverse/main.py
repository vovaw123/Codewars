class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
#     old = []
#     while head is not None:
#         old.append(int(head.data))
#         head = head.next
#         head = None
#     old.reverse()
#     for value in old:
#         node = Node(value)
#         node.next = head
#         head = node

#     return head
    if head is None or head.next is None:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head