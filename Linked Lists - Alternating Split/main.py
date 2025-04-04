class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise Exception()
    nodes = []
    current = head
    while current is not None:
        nodes.append(current)
        current = current.next

    first_list = []
    second_list = []

    counter = 0

    for node in nodes:
        if counter % 2 == 0:
            first_list.append(node)
        else:
            second_list.append(node)
        counter += 1

    for i in range(len(first_list) - 1):
        first_list[i].next = first_list[i + 1]
    if first_list:
        first_list[-1].next = None


    for i in range(len(second_list) - 1):
        second_list[i].next = second_list[i + 1]
    if second_list:
        second_list[-1].next = None

    return Context(first_list[0], second_list[0])