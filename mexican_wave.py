import unittest


def wave(string) -> []:
    wave_strings = []
    for index, char in enumerate(string):
        if not char.isspace():
            wave_string = capitalize_nth(string, index)
            wave_strings.append(wave_string)
    return wave_strings


def capitalize_nth(s, n):
    return s[:n].lower() + s[n:].capitalize()


class TestStringMethods(unittest.TestCase):

    def test_it_should_identify_unique_number(self):
        self.assertEqual(wave("codewars"),
                         ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs",
                          "codewarS"])


if __name__ == '__main__':
    unittest.main()
