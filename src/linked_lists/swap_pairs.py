from ...src.data_structures.nodes import LinkNode


def swap_pairs(head: LinkNode) -> LinkNode:

    new_head = head.next
    a, b, prev = head, head.next,  None

    while a and b:
        a.next = b.next
        b.next = a

        if prev:
            prev.next = b
        if not a.next:
            break
        b = a.next.next
        prev = a
        a = a.next

    return new_head
