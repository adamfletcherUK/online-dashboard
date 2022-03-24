import unittest

from src.pages.exp import trim_filename


class MyTestCase(unittest.TestCase):
    def test_trim_filename(self):
        long_text = "abcdefg"
        short_text = "cd"
        trimmed_text = trim_filename(long_text, 2)
        assert trimmed_text == short_text


if __name__ == '__main__':
    unittest.main()
