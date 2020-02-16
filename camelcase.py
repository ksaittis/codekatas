import unittest


def camel_case(string: str) -> str:
    if not string:
        return ''
    camel_case_result = ''
    for word in string.strip().split(' '):
        camel_case_result += convert_to_camel_case(word)
    return camel_case_result


def convert_to_camel_case(word: str) -> str:
    return word[0].upper() + word[1:]


class TestCamelCase(unittest.TestCase):

    def test_it_should_make_string_to_camel_case(self):
        self.assertEqual('', camel_case(''))
        self.assertEqual('Hello', camel_case('hello'))
        self.assertEqual('Hello', camel_case('Hello'))

    def test_it_should_camel_case_multiple_words(self):
        self.assertEqual("TestCase", camel_case("test case"))
        self.assertEqual("CamelCaseMethod", camel_case("camel case method"))

    def test_it_should_trim_extra_leading_trailing_spaces(self):
        self.assertEqual('SayHello', camel_case("say hello "))
        self.assertEqual("CamelCaseWord", camel_case(" camel case word"))
