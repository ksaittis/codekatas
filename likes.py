import unittest


def likes(people_who_liked_it: []) -> str:
    number_of_people_who_liked_it: int = len(people_who_liked_it)
    if number_of_people_who_liked_it == 0:
        return 'no one likes this'
    if number_of_people_who_liked_it == 1:
        return f'{people_who_liked_it[0]} likes this'
    if number_of_people_who_liked_it == 2:
        return f'{people_who_liked_it[0]} and {people_who_liked_it[1]} like this'
    if number_of_people_who_liked_it == 3:
        return f'{people_who_liked_it[0]}, {people_who_liked_it[1]} and {people_who_liked_it[2]} like this'
    return f'{people_who_liked_it[0]}, {people_who_liked_it[1]} and {len(people_who_liked_it) - 2} others like this'


class TestLikes(unittest.TestCase):

    def test_it_should_print_no_one_likes_this(self):
        self.assertEqual(likes([]), 'no one likes this')

    def test_it_should_print_someone_likes_this(self):
        self.assertEqual(likes(['Peter']), 'Peter likes this')

    def test_it_should_print_2_people_like_this(self):
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')

    def test_it_should_print_3_people_lie_this(self):
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')

    def test_it_should_print_2_people_if_more_than_4_people_like_it(self):
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
