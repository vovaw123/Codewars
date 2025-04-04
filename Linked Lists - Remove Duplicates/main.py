class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
#     old = []
#     while head is not None:
#         old.append(int(head.data))
#         head = head.next
#         head = None
    cur = head
    while cur is not None and cur.next is not None:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head