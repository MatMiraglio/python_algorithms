from Node import Node

def removeNth(head, n):
    dummy = Node(0)
    dummy.next = head
    first, second = dummy, dummy

    for _ in range(n + 1):
        first = first.next
    
    while first != None:
        first = first.next
        second = second.next

    second.next = second.next.next 

    return dummy.next

def removeNthFromEnd(head, n):
    if head.next == None:
            return None

    stack = []
    current_node = head

    while current_node:
        stack.append(current_node)
        current_node = current_node.next
    
    if len(stack) == n:
        return head.next
    
    
    node_after_n = None
    node_before_n = None

    for _ in range(n - 1):
        node_after_n = stack.pop()

    for _ in range(2):
        node_before_n = stack.pop()

    node_before_n.next = node_after_n

    return head
