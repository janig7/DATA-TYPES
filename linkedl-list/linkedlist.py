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
    
    def add_after(self, target_node_data, data):
        if not self.head:
            raise Exception('List is empty!')

        new_node = Node(data=data)

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        
        raise Exception(f'Node with data {target_node_data} not found!')

    def add_before(self, target_node_data, data):
        if not self.head:
            raise Exception('List is empty!')

        

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
        
        raise Exception(f'Node with data {target_node_data} not found!')





if __name__ == "__main__":
    linked_list = LinkedList([1,2,3, 2, 3,4,5, 4])
    linked_list.add_last(2)
    linked_list.add_before(2, 8)
    linked_list.add_after(3, 2137)

    print(linked_list)
