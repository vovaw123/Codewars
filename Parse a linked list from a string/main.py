class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
def linked_list_from_string(s):
    s_list = s.split(" -> ")
    s_list_reversed = []
    for i in range(len(s_list)-1, -1, -1):
        s_list_reversed.append(s_list[i])
    s_list_reversed.remove("None")
    head = None
    for i in s_list_reversed:
        head = Node(int(i), head)
    return head