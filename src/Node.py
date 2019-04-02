import unittest

class Node:

    def __init__(self, x):
        self.val = x
        self.next = None
        self._iterator = self

    def __str__(self): 
       return 'Node: %s' % (self.val)

    def __len__(self):
        length = 1
        next = self.next

        while next:
            length += 1
            next = next.next 
            
        return length

    def __iter__(self):
        return self

    def __next__(self):
        if self._iterator:
            current_node = self._iterator
            self._iterator = self._iterator.next
            return current_node
        else:
            raise StopIteration
        

    @staticmethod
    def create_linked_list(length : int):
        head = Node(0)
        node = head
        for _ in range(1, length):
            node.next = Node(_)
            node = node.next

        return head

class Test(unittest.TestCase):
    
    def test_create(self):
        expected_size = 8
        actual_size = 0
        head = Node.create_linked_list(expected_size)
        while head:
            actual_size += 1
            head = head.next
        
        assert expected_size == actual_size

    def test_len(self):
        size = 8
        head = Node.create_linked_list(size)
        assert len(head) == size

    def test_iter(self):
        size = 3
        head = Node.create_linked_list(size)
        for i, node in enumerate(head):
           assert node.val == i

if __name__ == '__main__':
    unittest.main()