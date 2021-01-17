class EmptyList(Exception):
    def __str__(self):
        return 'List is empty'


class DataNotFound(Exception):
    def __init__(self, target_node_data):
        self.target_node_data = target_node_data

    def  __str__(self):
        return f'Node with data {self.target_node_data} not found!'

