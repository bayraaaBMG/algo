import unittest

def insertion_sort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j -1
            A[j + 1] = key

    class TestInsertionSort(unittest.TestCase):
        def test_insertion_sort(self):
            lst = [12, 3, 7, 9, 14, 6, 11, 2]
            insertion_sort(lst, len(1))
            self.assertEqual([2, 3, 6, 7, 9, 11, 12, 14], lst)

    if __name__ == "__main__":
        unittest.main()