from . import sortable_array
class QuickSort(sortable_array.SortableArray):
    def __init__(self, arrlen=256):
        super().__init__(arrlen)

    def sort_func(self):
        self.sort_helper(0,self.arrLen-1)
        if self.isSorting:
            self.isSorted = True
        self.isSorting = False

    def sort_helper(self,start,idx):

        seeker, to_swap = start,start

        if idx > start:
            for i in range(start,idx+1):
                if not self.isSorting:
                    return
                if not super().compare_idx(i,idx):
                    super().sim_sleep()
                    super().swapElement(seeker,to_swap)
                    if i != idx:
                        to_swap += 1
                    seeker += 1
                else:
                    seeker += 1
            self.sort_helper(start,to_swap-1)
            self.sort_helper(to_swap+1,idx)

