from app.main import get_short
import unittest

class TestGetShort(unittest.TestCase):
    def test_len(self):
        s = get_short()
        self.assertEqual(len(s), 6)

if __name__ == '__main__':
    unittest.main()