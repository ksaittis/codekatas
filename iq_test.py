import unittest


def iq_test(numbers):
    pass


def identify_rate(array: []) -> int:
    rate = 0
    new_rate = 0
    for i in range(len(array) - 1):
        rate = array[i + 1] - array[i]


class TestStringMethods(unittest.TestCase):

    def test_it_should_identify_rate(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
