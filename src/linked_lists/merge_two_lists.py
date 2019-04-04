from ..data_structures.nodes import LinkNode

def mergeTwoLists(l1: LinkNode, l2: LinkNode) -> LinkNode:        
    dummy = current = LinkNode(0)

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
