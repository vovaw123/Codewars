#Linked Lists - Sorted Insert
""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
#     result = []
#     while head is not None:
#         result.append(str(head.data))
#         head = head.next
#     result.append(int(data))
#     result.remove("None")
    
#     result.sort()
#     rev_res = []
#     for i in range(len(result)-1, -1, -1):
#         rev_res.append(result[i])
#     head = None
#     for i in rev_res:
#         head = Node(int(i), head)
#     return head
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    result.append(data)
    
    result.sort()
    
    head = None
    for i in reversed(result):
        node = Node(i)
        node.next = head
        head = node
    return head