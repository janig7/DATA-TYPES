from node import Node


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(None)
        return ' -> '.join((f'{elem}' for elem in nodes))

    def add_first(self, data):
        node = Node(data=data)

        node.next = self.head
        self.head = node

    def add_last(self, data):
        node = Node(data=data)
        if not self.head:
            self.head = node

        for current_node in self:
            pass
        current_node.next = node


if __name__ == "__main__":
    linked_list = LinkedList([[1,2,3], 2, [3,4,5], 4])
    linked_list.add_last(2)
    linked_list.add_first(3)
    print(linked_list)
