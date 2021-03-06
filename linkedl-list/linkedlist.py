from node import Node
from linked_list_exceptions import EmptyList, DataNotFound


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

    def add_after(self, target_node_data, data):
        if not self.head:
            raise EmptyList

        new_node = Node(data=data)

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise DataNotFound(target_node_data)

    def add_before(self, target_node_data, data):
        if not self.head:
            raise EmptyList

        if self.head.data == target_node_data:
            return self.add_first(data)

        new_node = Node(data=data)
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise DataNotFound(target_node_data)

    def remove_node(self, target_node_data, data):
        if not self.head:
            raise EmptyList

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head

        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise DataNotFound(target_node_data)


if __name__ == "__main__":
    linked_list = LinkedList([3, 9, 6])
    linked_list.add_before(2, 8)

    print(linked_list)
