class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        # Increment counter
        self.count += 1
        # Jump to the next element
        try:
            return next(self.iterator)
        except StopIteration:
            self.count -= 1
            raise

    def get_count(self):
        return self.count
