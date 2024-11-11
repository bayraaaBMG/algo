import unittest

def find_max(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)
    return max(left_max, right_max)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l1 = arr[:mid]
        l2 = arr[mid:]

        merge_sort(l1)
        merge_sort(l2)

        i = j = k = 0

        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                arr[k] = l1[i]
                i += 1
            else:
                arr[k] = l2[j]
                j += 1
            k += 1

        while i < len(l1):
            arr[k] = l1[i]
            i += 1
            k += 1

        while j < len(l2):
            arr[k] = l2[j]
            j += 1
            k += 1

def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)
    else:
        return binary_search(arr, low, mid - 1, target)

class TestLab2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # "input.txt" файлаас уншиж байна
        with open("input.txt", "r") as file:
            data = file.readline().split("\t")
            cls.arr = cls.parse_array(data[0])  # Жинхэнэ массив
            cls.corAns = cls.parse_array(data[1])  # Эрэмбэлэгдсэн массив
            cls.target = int(data[2].strip())  # Зорилтот үнэ цэнэ
    @staticmethod
    def parse_array(array_str):
        array_str = array_str.replace("[", "").replace("]", "").strip()
        return list(map(int, array_str.split(',')))

    def test_insertion_sort(self):
        arr_copy = self.arr[:]
        insertion_sort(arr_copy)
        self.assertEqual(arr_copy, self.corAns)

    def test_merge_sort(self):
        arr_copy = self.arr[:]
        merge_sort(arr_copy)
        self.assertEqual(arr_copy, self.corAns)

    def test_find_max(self):
        max_element = find_max(self.arr, 0, len(self.arr) - 1)
        self.assertEqual(max_element, max(self.arr))

    def test_binary_search(self):
        sorted_arr = sorted(self.arr)
        result_index = binary_search(sorted_arr, 0, len(sorted_arr) - 1, self.target)
        expected_index = np.searchsorted(sorted_arr, self.target) - 1
        self.assertEqual(result_index, expected_index)

if __name__ == "__main__":
    unittest.main()
