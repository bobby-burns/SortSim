from . import sortable_array

    
class BubbleSort(sortable_array.SortableArray):
    def __init__(self, arrlen=256):
        super().__init__(arrlen)

    def sort_func(self):
        swps = self.arrLen
        while swps > 1:
            swps = self.arrLen
            if not self.isSorting:
                return
            for i in range(self.arrLen - 1):
                if super().compare_idx(i,i+1):
                    super().sim_sleep()
                    super().swapElement(i,i+1)
                else:
                    swps -= 1
        self.isSorted = True
        self.isSorting = False
        return
