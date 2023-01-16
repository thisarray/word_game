"""Python 3 script to print a list of words to standard output."""

import string
import unittest

LETTER_SET = frozenset(string.ascii_lowercase)
"""frozenset of string lowercase letters."""

def is_valid(word, length):
    """Return True if word is valid."""
    if not isinstance(word, str):
        return False
    if len(word) != length:
        return False
    for letter in word.lower():
        if letter not in LETTER_SET:
            return False
    return True


class _UnitTest(unittest.TestCase):
    def test_constants(self):
        """Test the module constants."""
        for value in [None, 42, '', 'A', 'BC']:
            self.assertNotIn(value, LETTER_SET)
        for value in string.ascii_uppercase:
            self.assertNotIn(value, LETTER_SET)
        for value in string.ascii_lowercase:
            self.assertIn(value, LETTER_SET)

    def test_is_valid(self):
        """Test if a word is valid."""
        for value in [None, 42, '', [], 'A', 'BC', 'FOO', 'FOOBAR',
                      'a', 'bc', 'foo', 'foobar']:
            self.assertFalse(is_valid(value, 4))
        for value in ['abcd', 'word']:
            self.assertTrue(is_valid(value, 4))

if __name__ == '__main__':
    import argparse
    import os.path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-l', '--length', type=int, default=4,
                        help='integer length of the words to print')
    parser.add_argument('path',
                        help='path to the full list of words')
    args = parser.parse_args()

    if os.path.isfile(args.path):
        with open(args.path, 'r') as f:
            for line in f:
                cleaned = line.strip().lower()
                if is_valid(cleaned, args.length):
                    print("  '{}',".format(cleaned))
    else:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(_UnitTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
