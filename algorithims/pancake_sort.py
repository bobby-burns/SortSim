from . import sortable_array
class PancakeSort(sortable_array.SortableArray):
    def __init__(self, arrlen=256):
        super().__init__(arrlen)

    def flip(self,k):
        left = 0
        while left < k:
            super().sim_sleep()
            super().swapElement(left,k)
            k -= 1
            left += 1

    def max_index(self,k):
        index = 0
        for i in range(k):
            if super().compare_idx(i,index):
                index = i
        return index

    def sort_func(self):
        n = len(self.arr)
        while n > 1:
            maxdex = self.max_index(n)
            if maxdex != n - 1:
                if maxdex != 0:
                    self.flip(maxdex)
                self.flip(n - 1)
            n -= 1
        self.isSorting = False
        self.isSorted = True
