from . import sortable_array


class RadixSort(sortable_array.SortableArray):
    def __init__(self, arrlen=256):
        super().__init__(arrlen)
    def sort_func(self):
        print("hi")

