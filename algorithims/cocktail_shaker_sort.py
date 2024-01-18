from . import sortable_array
class CockTailShakerSort(sortable_array.SortableArray):
    def __init__(self, arrlen=256):
        super().__init__(arrlen)

    def sort_func(self):
        swap = True
        startIdx = 0
        endIdx = self.arrLen-1
        while swap:
            swap = False

            for i in range(startIdx,endIdx):
                super().sim_sleep()
                if super().compare_idx(i,i+1):
                    swap = True
                    super().swapElement(i,i+1)
            endIdx -= 1
            if not swap:
                break

            for i in range(endIdx,startIdx,-1):
                super().sim_sleep()
                if super().compare_idx(i-1,i):
                    swap = True
                    super().swapElement(i-1,i)
            startIdx += 1

        self.isSorting = False
        self.isSorted = True
