class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        return cls(arr[0], cls.from_array(arr[1::])) if arr else None

    def filter(self, fn):
        """construct new algebraic list containing only elements
        that satisfy the predicate
        """
        if fn(self.head):
            return Cons(self.head, self.tail and self.tail.filter(fn))
        else:
            return self.tail and self.tail.filter(fn)

    def map(self, fn):
        """construct a new algebraic list containing all elements
        resulting from applying the mapper function to a list.
         """
        if self.tail is not None:
            self.head = fn(self.head)
            self.tail.map(fn)
            return self
        else:
            self.head = fn(self.head)
            return self


if __name__ == '__main__':
    print(Cons.from_array([1, 2, 3, 4, 5]).filter(lambda x: x > 3).to_array())
