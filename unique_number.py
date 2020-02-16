import unittest


def find_uniq(arr) -> int:
    for i in arr:
        occurrences = arr.count(i)
        if occurrences == 1:
            return i
    return arr[0]


def find_uniq_v2(arr) -> int:
    return [x for x in arr if arr.count(x) == 1][0]


def find_uniq_v3(arr) -> int:
    for i in set(arr):
        if arr.count(i) == 1:
            return i


class TestStringMethods(unittest.TestCase):

    def test_it_should_identify_unique_number(self):
        self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)
        self.assertEqual(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
        self.assertEqual(find_uniq([3, 10, 3, 3, 3]), 10)

    def test_it_should_identify_unique_number_v2(self):
        self.assertEqual(find_uniq_v2([1, 1, 1, 2, 1, 1]), 2)
        self.assertEqual(find_uniq_v2([0, 0, 0.55, 0, 0]), 0.55)
        self.assertEqual(find_uniq_v2([3, 10, 3, 3, 3]), 10)

    def test_it_should_identify_unique_number_v3(self):
        self.assertEqual(find_uniq_v3([1, 1, 1, 2, 1, 1]), 2)
        self.assertEqual(find_uniq_v3([0, 0, 0.55, 0, 0]), 0.55)
        self.assertEqual(find_uniq_v3([3, 10, 3, 3, 3]), 10)


if __name__ == '__main__':
    unittest.main()
