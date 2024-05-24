class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        if item in self:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)
        else:
            print(
                "Attempted to remove [{}], but it was not found in the list."
                .format(item))

    def pop(self, index=-1):
        try:
            item = self[index]
            super().pop(index)
            print("Popped [{}] from the list.".format(item))
        except IndexError:
            print("Attempted to pop index [{}], but it was out of range."
                  .format(index))
