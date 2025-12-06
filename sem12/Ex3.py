import random
import unittest
arr = [1, 2, -1, -2, 0]


def quick_sort(ll):
    if not isinstance(ll, list):
        return ('input data should be list')
    n = len(ll)
    if n == 1:
        return ll
    elif n == 0:
        return []
    less = []
    more = []
    middle = []
    pivot = ll[random.randint(0, n - 1)]
    for el in ll:
        if el < pivot:
            less.append(el)
        elif el > pivot:
            more.append(el)
        else:
            middle.append(el)
    return quick_sort(less) + middle + quick_sort(more)


print(quick_sort(arr))


class TestEqualList(unittest.TestCase):
    def test_equal_list(self):
        self.assertEqual(quick_sort([1, 1, 1, 1]), [1, 1, 1, 1],
                         "should be [1, 1, 1, 1]")


class TestDifList(unittest.TestCase):
    def test_dif_list(self):
        self.assertEqual(quick_sort([1, -1, 3, -9]), [-9, -1, 1, 3],
                         "should be [-9, -1, 1, 3]")


class TestData(unittest.TestCase):
    def test_data(self):
        self.assertEqual(quick_sort('string'), 'input data should be list',
                         'input data should be list')


class TestSingle(unittest.TestCase):
    def test_single(self):
        self.assertEqual(quick_sort([9]), [9], 'should be 9')
