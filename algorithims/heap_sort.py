from . import sortable_array
class HeapSort(sortable_array.SortableArray):
    def __init__(self, arrlen=256):
        super().__init__(arrlen)

    def sort_func(self):
        start = self.arrLen // 2
        end = self.arrLen

        while end > 1:
            if start > 0:
                start -= 1
            else:
                end -= 1
                super().swapElement(end,0)

            root = start
            while (2 * root + 1) < end:
                super().sim_sleep()
                child = (2 * root + 1)
                if child+1 < end and super().compare_idx(child+1,child):
                    child += 1
                if super().compare_idx(child,root):
                    super().swapElement(root,child)
                    root = child
                else:
                    break
        self.isSorting = False
        self.isSorted = True
