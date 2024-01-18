import algorithims as algs
import inspect
import unittest

classes = []
for _,obj in inspect.getmembers(algs):
    if inspect.ismodule(obj):
        for name,obj in inspect.getmembers(obj):
            if inspect.isclass(obj) and name != "SortableArray":
                classes.append(obj)

sorters = [i() for i in classes]


arrlen = algs.sortable_array.SortableArray().arrLen

sorted_arr = [i for i in range(arrlen)]

class AlgorithimTestCase(unittest.TestCase):
    def test_algs(self):
        for alg in sorters:
            with self.subTest(msg=alg.__class__.__name__):
                alg.shouldSleep = False
                alg.isSorting = True
                alg.sort_func()
                self.assertListEqual(alg.arr,sorted_arr)

