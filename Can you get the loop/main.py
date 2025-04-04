def loop_size(node):
#     seen = []
    
#     current = node
#     while True:
#         if current in seen:
#             first_index = seen.index(current)
#             return len(seen) - first_index
#         seen.append(current)
#         current = current.next

    seen = set()
    current = node
    while current not in seen:
        seen.add(current)
        current = current.next

    loop_start = current
    current = current.next
    length = 1
    while current != loop_start:
        current = current.next
        length += 1

    return length