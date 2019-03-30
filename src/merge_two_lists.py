from Node import Node


def mergeTwoLists(l1: Node, l2: Node) -> Node:        
    dummy = current = Node(0)

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2    

    return dummy.next

first = Node.create_linked_list(2)
second = Node.create_linked_list(3)

result = mergeTwoLists(first, second)

assert len(result) == 5