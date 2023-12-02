import unittest
from quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    # 空
    def test_empty_array(self):
        arr = []
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, [])
    # 单个元素
    def test_single_element_array(self):
        arr = [1]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, [1])
    # 普通序列
    def test_sort_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    # 添加更多的测试用例

if __name__ == '__main__':
    unittest.main()
