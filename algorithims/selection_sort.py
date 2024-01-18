from . import sortable_array
class SelectionSort(sortable_array.SortableArray):
    def __init__(self, arrlen=256):
        super().__init__(arrlen)
        self.root = None



    def sort_func(self):
        for i in range(self.arrLen-1):
            lowest = i
            for j in range(i+1,self.arrLen):
                super().sim_sleep()
                if super().compare_idx(lowest,j):
                    lowest = j
            super().swapElement(i,lowest)
        self.isSorting = False
        self.isSorted = True
