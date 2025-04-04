
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise Exception()
    values = []
    current = source
    while current is not None:
        values.append(current.data)
        current = current.next

    first_value = values[0]

    source = source.next
    new_node = Node(first_value)
    new_node.next = dest
    dest = new_node

    return Context(source, dest)