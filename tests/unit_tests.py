import unittest
import anagrams


phrase_cases = [
    ("abcd efgh", "dcba hgfe"),
    ("a1bcd efg!h", "d1cba hgf!e"),
    ("34124 43254", "34124 43254"),
    ("fg1S, 12E#q", "Sg1f, 12q#E")
]


class TestAnagrams(unittest.TestCase):
    def test_str_reverse(self):
        pass

    def test_phrase_anagram(self):
        for text, reversed_text in phrase_cases:
            with self.subTest():
                message = "Default text: " + text + " -- reversed text: " + \
                          reversed_text
                self.assertEqual(anagrams.phrase_anagram(text), reversed_text,
                                 message)
