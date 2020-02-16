import unittest


def get_weird_case(word) -> str:
    char_string = ''
    for index, char in enumerate(word):
        if is_even(index):
            char_string += char.upper()
        else:
            char_string += char
    return char_string


def is_even(num) -> bool:
    return num % 2 == 0


def to_weird_case(string):
    words = string.split()
    weird_case_words = []
    for word in words:
        weird_case_word = get_weird_case(word)
        weird_case_words.append(weird_case_word)
    return weird_case_words


def to_weird_case_v2(string) -> str:
    counter = 0
    weird_case_result = ''
    for char in string:
        if char.isspace():
            counter = 0
            weird_case_result += ' '
            continue
        if is_even(counter):
            weird_case_result += char.upper()
            counter += 1
        else:
            weird_case_result += char
            counter += 1
    return weird_case_result

class TestStringMethods(unittest.TestCase):

    def test_it_should_identify_unique_number(self):
        self.assertEqual(to_weird_case_v2('This'), 'ThIs')
        self.assertEqual(to_weird_case_v2('is'), 'Is')
        self.assertEqual(to_weird_case_v2('This is a test'), 'ThIs Is A TeSt')
