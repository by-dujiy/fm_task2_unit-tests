import unittest
from main import msg_to_str

str_cases = [
    ('abcd.', 'dcba.'),
    ('efg!h', 'hgf!e'),
    ('Фб-2!', 'бФ-2!'),
    ('12E#q', '12q#E'),
]

phrase_cases = [
    ("abcd. e*fgh", "dcba. h*gfe"),
    ("a1bcd efg!h", "d1cba hgf!e"),
    ("Фб-2! Ёэ:в%", "бФ-2! вэ:Ё%"),
    ("fg1S, 12E#q", "Sg1f, 12q#E")
]

a = '     '
b = '     '


class TestAnagrams(unittest.TestCase):
    def test_str_reverse(self):
        for text, reversed_text in str_cases:
            with self.subTest():
                self.assertEqual(msg_to_str(text), reversed_text)

    def test_phrase_anagram(self):
        for text, reversed_text in phrase_cases:
            with self.subTest():
                self.assertEqual(msg_to_str(text), reversed_text)

    def test_str_reverse_isNot(self):
        self.assertIsNot(msg_to_str('1234'), 1234)

    def test_is_str(self):
        self.assertEqual(msg_to_str(1234), '1234')

    def test_whitespace(self):
        self.assertEqual(msg_to_str(a), b)


if __name__ == '__main__':
    unittest.main()
