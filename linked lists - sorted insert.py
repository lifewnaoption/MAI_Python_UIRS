class Node(object):
    def __init__(self, data, nxt=None):
        self.data, self.next = data, nxt


def sorted_insert(head, data):
    if head is None or head.data > data:
        return Node(data, head)
    node = head
    while node.next and node.next.data < data:
        node = node.next
    node.next = Node(data, node.next)
    return head