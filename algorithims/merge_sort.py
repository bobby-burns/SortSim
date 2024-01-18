from . import sortable_array
class MergeSort(sortable_array.SortableArray):
    def __init__(self, arrlen=256):
        super().__init__(arrlen)

    def sort_func(self):
        self.sort_helper(0,self.arrLen-1)
        self.isSorting = False
        self.isSorted = True

    def sort_helper(self,l,r):

       if (l < r):
     
            # Same as (l + r) / 2, but avoids overflow
            # for large l and r
            m = l + (r - l) // 2
     
            # Sort first and second halves
            self.sort_helper( l, m)
            self.sort_helper( m + 1, r)
     
            self.merge( l, m, r)
    def merge(self,start,mid,end):
        start2 = mid + 1
 
        # If the direct merge is already sorted
        self.arrayAccesses += 2
        self.comparisons += 1
        if (self.arr[mid] <= self.arr[start2]):
            return
     
        # Two pointers to maintain start
        # of both arrays to merge
        while (start <= mid and start2 <= end):
            super().sim_sleep()
            # If element 1 is in right place
            if (not super().compare_idx(start,start2)):
                start += 1
            else:
                self.arrayAccesses += 1
                value = self.arr[start2]
                index = start2
     
                # Shift all the elements between element 1
                # element 2, right by 1.
                while (index != start):
                    super().swapElement(index,index-1)
                    index -= 1
     
                self.arrayAccesses += 1
                self.arr[start] = value
     
                # Update all the pointers
                start += 1
                mid += 1
                start2 += 1
