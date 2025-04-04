class Node:
    def __init__(self, next=None):
        self.next = next
        
from preloaded import Node

def swap_pairs(head):
    if head is None:
        return None
    nodes = []
    current = head
    while current is not None:
        nodes.append(current)
        current = current.next

    swapped = []
    pair = []
    counter = 0

    for node in nodes:
        pair.append(node)
        counter += 1

        if counter == 2:
            swapped.append(pair[1])
            swapped.append(pair[0])
            pair = []
            counter = 0

    if pair:
        swapped.append(pair[0])

    for i in range(len(swapped) - 1):
        swapped[i].next = swapped[i + 1]
    swapped[-1].next = None

    return swapped[0]