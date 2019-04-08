from ..data_structures.nodes import BinaryNode


def binary_tree(elements: []) -> BinaryNode:
    return create_BST(elements, 0, len(elements) - 1)


def create_BST(elements, start, end) -> BinaryNode:
    if end < start:
        return

    mid = int((start + end) / 2)
    node = BinaryNode(elements[mid])
    node.left = create_BST(elements, start, mid - 1)
    node.right = create_BST(elements, mid + 1, end)
    return node
